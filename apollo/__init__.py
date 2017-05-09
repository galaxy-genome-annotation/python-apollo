import requests
import json
import os
import collections
try:
    import StringIO as io
except:
    import io
import logging
import time
import argparse
from abc import abstractmethod
from BCBio import GFF
from Bio import SeqIO
logging.getLogger("requests").setLevel(logging.CRITICAL)
log = logging.getLogger()


#############################################
#      BEGIN IMPORT OF CACHING LIBRARY      #
#############################################
# This code is licensed under the MIT       #
# License and is a copy of code publicly    #
# available in rev.                         #
# e27332bc82f4e327aedaec17c9b656ae719322ed  #
# of https://github.com/tkem/cachetools/    #
#############################################

class DefaultMapping(collections.MutableMapping):

    __slots__ = ()

    @abstractmethod
    def __contains__(self, key):  # pragma: nocover
        return False

    @abstractmethod
    def __getitem__(self, key):  # pragma: nocover
        if hasattr(self.__class__, '__missing__'):
            return self.__class__.__missing__(self, key)
        else:
            raise KeyError(key)

    def get(self, key, default=None):
        if key in self:
            return self[key]
        else:
            return default

    __marker = object()

    def pop(self, key, default=__marker):
        if key in self:
            value = self[key]
            del self[key]
        elif default is self.__marker:
            raise KeyError(key)
        else:
            value = default
        return value

    def setdefault(self, key, default=None):
        if key in self:
            value = self[key]
        else:
            self[key] = value = default
        return value


DefaultMapping.register(dict)


class _DefaultSize(object):
    def __getitem__(self, _):
        return 1

    def __setitem__(self, _, value):
        assert value == 1

    def pop(self, _):
        return 1


class Cache(DefaultMapping):
    """Mutable mapping to serve as a simple cache or cache base class."""

    __size = _DefaultSize()

    def __init__(self, maxsize, missing=None, getsizeof=None):
        if missing:
            self.__missing = missing
        if getsizeof:
            self.__getsizeof = getsizeof
            self.__size = dict()
        self.__data = dict()
        self.__currsize = 0
        self.__maxsize = maxsize

    def __repr__(self):
        return '%s(%r, maxsize=%r, currsize=%r)' % (
            self.__class__.__name__,
            list(self.__data.items()),
            self.__maxsize,
            self.__currsize,
        )

    def __getitem__(self, key):
        try:
            return self.__data[key]
        except KeyError:
            return self.__missing__(key)

    def __setitem__(self, key, value):
        maxsize = self.__maxsize
        size = self.getsizeof(value)
        if size > maxsize:
            raise ValueError('value too large')
        if key not in self.__data or self.__size[key] < size:
            while self.__currsize + size > maxsize:
                self.popitem()
        if key in self.__data:
            diffsize = size - self.__size[key]
        else:
            diffsize = size
        self.__data[key] = value
        self.__size[key] = size
        self.__currsize += diffsize

    def __delitem__(self, key):
        size = self.__size.pop(key)
        del self.__data[key]
        self.__currsize -= size

    def __contains__(self, key):
        return key in self.__data

    def __missing__(self, key):
        value = self.__missing(key)
        try:
            self.__setitem__(key, value)
        except ValueError:
            pass  # value too large
        return value

    def __iter__(self):
        return iter(self.__data)

    def __len__(self):
        return len(self.__data)

    @staticmethod
    def __getsizeof(value):
        return 1

    @staticmethod
    def __missing(key):
        raise KeyError(key)

    @property
    def maxsize(self):
        """The maximum size of the cache."""
        return self.__maxsize

    @property
    def currsize(self):
        """The current size of the cache."""
        return self.__currsize

    def getsizeof(self, value):
        """Return the size of a cache element's value."""
        return self.__getsizeof(value)


class _Link(object):

    __slots__ = ('key', 'expire', 'next', 'prev')

    def __init__(self, key=None, expire=None):
        self.key = key
        self.expire = expire

    def __reduce__(self):
        return _Link, (self.key, self.expire)

    def unlink(self):
        next = self.next
        prev = self.prev
        prev.next = next
        next.prev = prev


class _Timer(object):

    def __init__(self, timer):
        self.__timer = timer
        self.__nesting = 0

    def __call__(self):
        if self.__nesting == 0:
            return self.__timer()
        else:
            return self.__time

    def __enter__(self):
        if self.__nesting == 0:
            self.__time = time = self.__timer()
        else:
            time = self.__time
        self.__nesting += 1
        return time

    def __exit__(self, *exc):
        self.__nesting -= 1

    def __reduce__(self):
        return _Timer, (self.__timer,)

    def __getattr__(self, name):
        return getattr(self.__timer, name)


class TTLCache(Cache):
    """LRU Cache implementation with per-item time-to-live (TTL) value."""

    def __init__(self, maxsize, ttl, timer=time.time, missing=None,
                 getsizeof=None):
        Cache.__init__(self, maxsize, missing, getsizeof)
        self.__root = root = _Link()
        root.prev = root.next = root
        self.__links = collections.OrderedDict()
        self.__timer = _Timer(timer)
        self.__ttl = ttl

    def __contains__(self, key):
        try:
            link = self.__links[key]  # no reordering
        except KeyError:
            return False
        else:
            return not (link.expire < self.__timer())

    def __getitem__(self, key, cache_getitem=Cache.__getitem__):
        try:
            link = self.__getlink(key)
        except KeyError:
            expired = False
        else:
            expired = link.expire < self.__timer()
        if expired:
            return self.__missing__(key)
        else:
            return cache_getitem(self, key)

    def __setitem__(self, key, value, cache_setitem=Cache.__setitem__):
        with self.__timer as time:
            self.expire(time)
            cache_setitem(self, key, value)
        try:
            link = self.__getlink(key)
        except KeyError:
            self.__links[key] = link = _Link(key)
        else:
            link.unlink()
        link.expire = time + self.__ttl
        link.next = root = self.__root
        link.prev = prev = root.prev
        prev.next = root.prev = link

    def __delitem__(self, key, cache_delitem=Cache.__delitem__):
        cache_delitem(self, key)
        link = self.__links.pop(key)
        link.unlink()
        if link.expire < self.__timer():
            raise KeyError(key)

    def __iter__(self):
        root = self.__root
        curr = root.next
        while curr is not root:
            # "freeze" time for iterator access
            with self.__timer as time:
                if not (curr.expire < time):
                    yield curr.key
            curr = curr.next

    def __len__(self):
        root = self.__root
        curr = root.next
        time = self.__timer()
        count = len(self.__links)
        while curr is not root and curr.expire < time:
            count -= 1
            curr = curr.next
        return count

    def __setstate__(self, state):
        self.__dict__.update(state)
        root = self.__root
        root.prev = root.next = root
        for link in sorted(self.__links.values(), key=lambda obj: obj.expire):
            link.next = root
            link.prev = prev = root.prev
            prev.next = root.prev = link
        self.expire(self.__timer())

    def __repr__(self, cache_repr=Cache.__repr__):
        with self.__timer as time:
            self.expire(time)
            return cache_repr(self)

    @property
    def currsize(self):
        with self.__timer as time:
            self.expire(time)
            return super(TTLCache, self).currsize

    @property
    def timer(self):
        """The timer function used by the cache."""
        return self.__timer

    @property
    def ttl(self):
        """The time-to-live value of the cache's items."""
        return self.__ttl

    def expire(self, time=None):
        """Remove expired items from the cache."""
        if time is None:
            time = self.__timer()
        root = self.__root
        curr = root.next
        links = self.__links
        cache_delitem = Cache.__delitem__
        while curr is not root and curr.expire < time:
            cache_delitem(self, curr.key)
            del links[curr.key]
            next = curr.next
            curr.unlink()
            curr = next

    def clear(self):
        with self.__timer as time:
            self.expire(time)
            Cache.clear(self)

    def get(self, *args, **kwargs):
        with self.__timer:
            return Cache.get(self, *args, **kwargs)

    def pop(self, *args, **kwargs):
        with self.__timer:
            return Cache.pop(self, *args, **kwargs)

    def setdefault(self, *args, **kwargs):
        with self.__timer:
            return Cache.setdefault(self, *args, **kwargs)

    def popitem(self):
        """Remove and return the `(key, value)` pair least recently used that
        has not already expired.

        """
        with self.__timer as time:
            self.expire(time)
            try:
                key = next(iter(self.__links))
            except StopIteration:
                raise KeyError('%s is empty' % self.__class__.__name__)
            else:
                return (key, self.pop(key))

    if hasattr(collections.OrderedDict, 'move_to_end'):
        def __getlink(self, key):
            value = self.__links[key]
            self.__links.move_to_end(key)
            return value
    else:
        def __getlink(self, key):
            value = self.__links.pop(key)
            self.__links[key] = value
            return value


#############################################
#       END IMPORT OF CACHING LIBRARY       #
#############################################


cache = TTLCache(
    100,  # Up to 100 items
    5 * 60  # 5 minute cache life
)
userCache = TTLCache(
    2,  # Up to 2 items
    60  # 1 minute cache life
)


class UnknownUserException(Exception):
    pass


def WAAuth(parser):
    parser.add_argument('apollo', help='Complete Apollo URL')
    parser.add_argument('username', help='WA Username')
    parser.add_argument('password', help='WA Password')


def OrgOrGuess(parser):
    parser.add_argument('--org_json', type=argparse.FileType("r"), help='Apollo JSON output, source for common name')
    parser.add_argument('--org_raw', help='Common Name')
    parser.add_argument('--org_id', help='Organism ID')


def CnOrGuess(parser):
    OrgOrGuess(parser)
    parser.add_argument('--seq_fasta', type=argparse.FileType("r"), help='Fasta file, IDs used as sequence sources')
    parser.add_argument('--seq_raw', nargs='*', help='Sequence Names')


def GuessOrg(args, wa):
    if args.org_json:
        orgs = [x.get('commonName', None)
                for x in json.load(args.org_json)]
        orgs = [x for x in orgs if x is not None]
        return orgs
    elif args.org_raw:
        org = args.org_raw.strip()
        if len(org) > 0:
            return [org]
        else:
            raise Exception("Organism Common Name not provided")
    elif args.org_id:
        return [wa.organisms.findOrganismById(args.org_id).get('commonName', None)]
    else:
        raise Exception("Organism Common Name not provided")


def GuessCn(args, wa):
    org = GuessOrg(args, wa)
    seqs = []
    if args.seq_fasta:
        # If we have a fasta, pull all rec ids from that.
        for rec in SeqIO.parse(args.seq_fasta, 'fasta'):
            seqs.append(rec.id)
    elif args.seq_raw:
        # Otherwise raw list.
        seqs = [x.strip() for x in args.seq_raw if len(x.strip()) > 0]

    return org, seqs


def AssertUser(user_list):
    if len(user_list) == 0:
        raise UnknownUserException()
    elif len(user_list) == 1:
        return user_list[0]
    else:
        raise Exception("Too many users!")


def AssertAdmin(user):
    if user.role == 'ADMIN':
        return True
    else:
        raise Exception("User is not an administrator. Permission denied")


class WebApolloInstance(object):

    def __init__(self, url, username, password):
        self.apollo_url = url
        self.username = username
        self.password = password

        self.annotations = AnnotationsClient(self)
        self.groups = GroupsClient(self)
        self.io = IOClient(self)
        self.organisms = OrganismsClient(self)
        self.users = UsersClient(self)
        self.metrics = MetricsClient(self)
        self.bio = RemoteRecord(self)
        self.status = StatusClient(self)
        self.canned_comments = CannedCommentsClient(self)
        self.canned_keys = CannedKeysClient(self)
        self.canned_values = CannedValuesClient(self)

    def __str__(self):
        return '<WebApolloInstance at %s>' % self.apollo_url

    def requireUser(self, email):
        cacheKey = 'user-list'
        try:
            # Get the cached value
            data = userCache[cacheKey]
        except KeyError:
            # If we hit a key error above, indicating that
            # we couldn't find the key, we'll simply re-request
            # the data
            data = self.users.loadUsers()
            userCache[cacheKey] = data

        return AssertUser([x for x in data if x.username == email])


class GroupObj(object):
    def __init__(self, **kwargs):
        self.name = kwargs['name']

        if 'id' in kwargs:
            self.groupId = kwargs['id']


class UserObj(object):
    ROLE_USER = 'USER'
    ROLE_ADMIN = 'ADMIN'

    def __init__(self, **kwargs):
        # Generally expect 'userId', 'firstName', 'lastName', 'username' (email)
        for attr in kwargs.keys():
            setattr(self, attr, kwargs[attr])

        if 'groups' in kwargs:
            groups = []
            for groupData in kwargs['groups']:
                groups.append(GroupObj(**groupData))
            self.groups = groups

        self.__props = kwargs.keys()

    def isAdmin(self):
        if hasattr(self, 'role'):
            return self.role == self.ROLE_ADMIN
        return False

    def refresh(self, wa):
        # This method requires some sleeping usually.
        newU = wa.users.loadUser(self).toDict()
        for prop in newU:
            setattr(self, prop, newU[prop])

    def toDict(self):
        data = {}
        for prop in self.__props:
            data[prop] = getattr(self, prop)
        return data

    def orgPerms(self):
        for orgPer in self.organismPermissions:
            if len(orgPer['permissions']) > 2:
                orgPer['permissions'] = json.loads(orgPer['permissions'])
                yield orgPer

    def __str__(self):
        return '<User %s: %s %s <%s>>' % (self.userId, self.firstName,
                                          self.lastName, self.username)


class Client(object):

    def __init__(self, webapolloinstance, **requestArgs):
        self._wa = webapolloinstance

        self.__verify = requestArgs.get('verify', True)
        self._requestArgs = requestArgs

        if 'verify' in self._requestArgs:
            del self._requestArgs['verify']

    def request(self, clientMethod, data, post_params={}, isJson=True):
        url = self._wa.apollo_url + self.CLIENT_BASE + clientMethod

        headers = {
            'Content-Type': 'application/json'
        }

        data.update({
            'username': self._wa.username,
            'password': self._wa.password,
        })

        r = requests.post(url, data=json.dumps(data), headers=headers,
                          verify=self.__verify, params=post_params, allow_redirects=False, **self._requestArgs)

        if r.status_code == 200 or r.status_code == 302:
            if isJson:
                d = r.json()
                if 'username' in d:
                    del d['username']
                if 'password' in d:
                    del d['password']
                return d
            else:
                return r.text

        # @see self.body for HTTP response body
        raise Exception("Unexpected response from apollo %s: %s" %
                        (r.status_code, r.text))

    def get(self, clientMethod, get_params):
        url = self._wa.apollo_url + self.CLIENT_BASE + clientMethod
        headers = {}

        r = requests.get(url, headers=headers, verify=self.__verify,
                         params=get_params, **self._requestArgs)
        if r.status_code == 200:
            d = r.json()
            if 'username' in d:
                del d['username']
            if 'password' in d:
                del d['password']
            return d
        # @see self.body for HTTP response body
        raise Exception("Unexpected response from apollo %s: %s" %
                        (r.status_code, r.text))


class MetricsClient(Client):
    CLIENT_BASE = '/metrics/'

    def getServerMetrics(self):
        return self.get('metrics', {})


class AnnotationsClient(Client):
    CLIENT_BASE = '/annotationEditor/'

    def _update_data(self, data):
        if not hasattr(self, '_extra_data'):
            raise Exception("Please call setSequence first")

        data.update(self._extra_data)
        return data

    def setSequence(self, sequence, organism):
        self._extra_data = {
            'sequence': sequence,
            'organism': organism,
        }

    def setDescription(self, featureDescriptions):
        data = {
            'features': featureDescriptions,
        }
        data = self._update_data(data)
        return self.request('setDescription', data)

    def setName(self, uniquename, name):
        # TODO
        data = {
            'features': [
                {
                    'uniquename': uniquename,
                    'name': name,
                }
            ],
        }
        data = self._update_data(data)
        return self.request('setName', data)

    def setNames(self, features):
        # TODO
        data = {
            'features': features,
        }
        data = self._update_data(data)
        return self.request('setName', data)

    def setStatus(self, statuses):
        # TODO
        data = {
            'features': statuses,
        }
        data = self._update_data(data)
        return self.request('setStatus', data)

    def setSymbol(self, symbols):
        data = {
            'features': symbols,
        }
        data.update(self._extra_data)
        return self.request('setSymbol', data)

    def getComments(self, feature_id):
        data = {
            'features': [{'uniquename': feature_id}],
        }
        data = self._update_data(data)
        return self.request('getComments', data)

    def addComments(self, feature_id, comments):
        # TODO: This is probably not great and will delete comments, if I had to guess...
        data = {
            'features': [
                {
                    'uniquename': feature_id,
                    'comments': comments
                }
            ],
        }
        data = self._update_data(data)
        return self.request('addComments', data)

    def addAttributes(self, feature_id, attributes):
        nrps = []
        for (key, values) in attributes.items():
            for value in values:
                nrps.append({
                    'tag': key,
                    'value': value
                })

        data = {
            'features': [
                {
                    'uniquename': feature_id,
                    'non_reserved_properties': nrps
                }
            ]
        }
        data = self._update_data(data)
        return self.request('addAttribute', data)

    def deleteAttribute(self, feature_id, key, value):
        data = {
            'features': [
                {
                    'uniquename': feature_id,
                    'non_reserved_properties': [
                        {'tag': key, 'value': value}
                    ]
                }
            ]
        }
        data = self._update_data(data)
        return self.request('addAttribute', data)
    def getFeatures(self):
        data = self._update_data({})
        return self.request('getFeatures', data)

    def getSequence(self, uniquename):
        data = {
            'features': [
                {'uniquename': uniquename}
            ]
        }
        data = self._update_data(data)
        return self.request('getSequence', data)

    def addFeature(self, feature, trustme=False):
        if not trustme:
            raise NotImplementedError("Waiting on better docs from project. If you know what you are doing, pass trustme=True to this function.")

        data = {
            'features': feature,
        }
        data = self._update_data(data)
        return self.request('addFeature', data)

    def addTranscript(self, transcript, trustme=False):
        if not trustme:
            raise NotImplementedError("Waiting on better docs from project. If you know what you are doing, pass trustme=True to this function.")

        data = {}
        data.update(transcript)
        data = self._update_data(data)
        return self.request('addTranscript', data)

    # addExon, add/delete/updateComments, addTranscript skipped due to docs

    def duplicateTranscript(self, transcriptId):
        data = {
            'features': [{'uniquename': transcriptId}]
        }

        data = self._update_data(data)
        return self.request('duplicateTranscript', data)

    def setTranslationStart(self, uniquename, start):
        data = {
            'features': [{
                'uniquename': uniquename,
                'location': {
                    'fmin': start
                }
            }]
        }
        data = self._update_data(data)
        return self.request('setTranslationStart', data)

    def setTranslationEnd(self, uniquename, end):
        data = {
            'features': [{
                'uniquename': uniquename,
                'location': {
                    'fmax': end
                }
            }]
        }
        data = self._update_data(data)
        return self.request('setTranslationEnd', data)

    def setLongestOrf(self, uniquename):
        data = {
            'features': [{
                'uniquename': uniquename,
            }]
        }
        data = self._update_data(data)
        return self.request('setLongestOrf', data)

    def setBoundaries(self, uniquename, start, end):
        data = {
            'features': [{
                'uniquename': uniquename,
                'location': {
                    'fmin': start,
                    'fmax': end,
                }
            }]
        }
        data = self._update_data(data)
        return self.request('setBoundaries', data)

    def getSequenceAlterations(self):
        data = {
        }
        data = self._update_data(data)
        return self.request('getSequenceAlterations', data)

    def setReadthroughStopCodon(self, uniquename):
        data = {
            'features': [{
                'uniquename': uniquename,
            }]
        }
        data = self._update_data(data)
        return self.request('setReadthroughStopCodon', data)

    def deleteSequenceAlteration(self, uniquename):
        data = {
            'features': [{
                'uniquename': uniquename,
            }]
        }
        data = self._update_data(data)
        return self.request('deleteSequenceAlteration', data)

    def flipStrand(self, uniquenames):
        data = {
            'features': [
                {'uniquename': x} for x in uniquenames
            ]
        }
        data = self._update_data(data)
        return self.request('flipStrand', data)

    def mergeExons(self, exonA, exonB):
        data = {
            'features': [
                {'uniquename': exonA},
                {'uniquename': exonB},
            ]
        }
        data = self._update_data(data)
        return self.request('mergeExons', data)

    # def splitExon(): pass

    def deleteFeatures(self, uniquenames):
        assert isinstance(uniquenames, collections.Iterable)
        data = {
            'features': [
                {'uniquename': x} for x in uniquenames
            ]
        }
        data = self._update_data(data)
        return self.request('deleteFeature', data)

    # def deleteExon(): pass

    # def makeIntron(self, uniquename, ): pass

    def getSequenceSearchTools(self):
        return self.get('getSequenceSearchTools', {})

    def getCannedComments(self):
        return self.get('getCannedComments', {})

    def searchSequence(self, searchTool, sequence, database):
        data = {
            'key': searchTool,
            'residues': sequence,
            'database_id': database,
        }
        return self.request('searchSequences', data)

    def getGff3(self, uniquenames):
        assert isinstance(uniquenames, collections.Iterable)
        data = {
            'features': [
                {'uniquename': x} for x in uniquenames
            ]
        }
        data = self._update_data(data)
        return self.request('getGff3', data, isJson=False)


class GroupsClient(Client):
    CLIENT_BASE = '/group/'

    def createGroup(self, name):
        data = {'name': name}
        return self.request('createGroup', data)

    def getOrganismPermissionsForGroup(self, group):
        data = {
            'id': group.groupId,
            'name': group.name,
        }
        return self.request('getOrganismPermissionsForGroup', data)

    def loadGroup(self, group):
        return self.loadGroupById(group.groupId)

    def loadGroupById(self, groupId):
        res = self.request('loadGroups', {'groupId': groupId})
        if isinstance(res, list):
            # We can only match one, right?
            return GroupObj(**res[0])
        else:
            return res

    def loadGroupByName(self, name):
        res = self.request('loadGroups', {'name': name})
        if isinstance(res, list):
            # We can only match one, right?
            return GroupObj(**res[0])
        else:
            return res

    def loadGroups(self, group=None):
        res = self.request('loadGroups', {})
        data = [GroupObj(**x) for x in res]
        if group is not None:
            data = [x for x in data if x.name == group]

        return data

    def deleteGroup(self, group):
        data = {
            'id': group.groupId,
            'name': group.name,
        }
        return self.request('deleteGroup', data)

    def updateGroup(self, group, newName):
        # TODO: Sure would be nice if modifying ``group.name`` would invoke
        # this?
        data = {
            'id': group.groupId,
            'name': newName,
        }
        return self.request('updateGroup', data)

    def updateOrganismPermission(self, group, organismName,
                                 administrate=False, write=False, read=False,
                                 export=False):
        data = {
            'groupId': group.groupId,
            'organism': organismName,
            'ADMINISTRATE': administrate,
            'WRITE': write,
            'EXPORT': export,
            'READ': read,
        }
        return self.request('updateOrganismPermission', data)

    def updateMembership(self, group, users):
        data = {
            'groupId': group.groupId,
            'user': [user.email for user in users]
        }
        return self.request('updateMembership', data)


class IOClient(Client):
    CLIENT_BASE = '/IOService/'

    def write(self, exportType='FASTA', seqType='peptide',
              exportFormat='text', sequences=None, organism=None,
              output='text', exportAllSequences=False,
              exportGff3Fasta=False):
        if exportType not in ('FASTA', 'GFF3'):
            raise Exception("exportType must be one of FASTA, GFF3")

        if seqType not in ('peptide', 'cds', 'cdna', 'genomic'):
            raise Exception("seqType must be one of peptide, cds, dna, genomic")

        if exportFormat not in ('gzip', 'text'):
            raise Exception("exportFormat must be one of gzip, text")

        if output not in ('file', 'text'):
            raise Exception("output must be one of file, text")

        data = {
            'type': exportType,
            'seqType': seqType,
            'format': exportFormat,
            'sequences': sequences,
            'organism': organism,
            'output': output,
            'exportAllSequences': exportAllSequences,
            'exportGff3Fasta': exportGff3Fasta,
        }

        return self.request('write', data, isJson=output == 'file')

    def download(self, uuid, outputFormat='gzip'):

        if outputFormat.lower() not in ('gzip', 'text'):
            raise Exception("outputFormat must be one of file, text")

        data = {
            'format': outputFormat,
            'uuid': uuid,
        }
        return self.request('write', data)


class StatusClient(Client):
    CLIENT_BASE = '/availableStatus/'

    def addStatus(self, value):
        data = {
            'value': value
        }

        return self.request('createStatus', data)

    def findAllStatuses(self):
        return self.request('showStatus', {})

    def findStatusByValue(self, value):
        statuses = self.findAllStatuses()
        statuses = [x for x in statuses if x['value'] == value]
        if len(statuses) == 0:
            raise Exception("Unknown status value")
        else:
            return statuses[0]

    def findStatusById(self, id_number):
        statuses = self.findAllStatuses()
        statuses = [x for x in statuses if str(x['id']) == str(id_number)]
        if len(statuses) == 0:
            raise Exception("Unknown ID")
        else:
            return statuses[0]

    def updateStatus(self, id_number, new_value):
        data = {
            'id': id_number,
            'new_value': new_value
        }

        return self.request('updateStatus', data)

    def deleteStatus(self, id_number):
        data = {
            'id': id_number
        }

        return self.request('deleteStatus', data)


class CannedCommentsClient(Client):
    CLIENT_BASE = '/cannedComment/'

    def addComment(self, comment, metadata=""):
        data = {
            'comment': comment,
            'metadata': metadata
        }

        return self.request('createComment', data)

    def findAllComments(self):
        return self.request('showComment', {})

    def findCommentByValue(self, value):
        comments = self.findAllComments()
        comments = [x for x in comments if x['comment'] == value]
        if len(comments) == 0:
            raise Exception("Unknown comment")
        else:
            return comments[0]

    def findCommentById(self, id_number):
        comments = self.findAllComments()
        comments = [x for x in comments if str(x['id']) == str(id_number)]
        if len(comments) == 0:
            raise Exception("Unknown ID")
        else:
            return comments[0]

    def updateComment(self, id_number, new_value, metadata=None):
        data = {
            'id': id_number,
            'new_comment': new_value
        }

        if metadata is not None:
            data['metadata'] = metadata

        return self.request('updateComment', data)

    def deleteComment(self, id_number):
        data = {
            'id': id_number
        }

        return self.request('deleteComment', data)


class CannedKeysClient(Client):
    CLIENT_BASE = '/cannedKey/'

    def addKey(self, key, metadata=""):
        data = {
            'key': key,
            'metadata': metadata
        }

        return self.request('createKey', data)

    def findAllKeys(self):
        return self.request('showKey', {})

    def findKeyByValue(self, value):
        keys = self.findAllKeys()
        keys = [x for x in keys if x['label'] == value]
        if len(keys) == 0:
            raise Exception("Unknown key")
        else:
            return keys[0]

    def findKeyById(self, id_number):
        keys = self.findAllKeys()
        keys = [x for x in keys if str(x['id']) == str(id_number)]
        if len(keys) == 0:
            raise Exception("Unknown ID")
        else:
            return keys[0]

    def updateKey(self, id_number, new_key, metadata=None):
        data = {
            'id': id_number,
            'new_key': new_key
        }

        if metadata is not None:
            data['metadata'] = metadata

        return self.request('updateKey', data)

    def deleteKey(self, id_number):
        data = {
            'id': id_number
        }

        return self.request('deleteKey', data)


class CannedValuesClient(Client):
    CLIENT_BASE = '/cannedValue/'

    def addValue(self, value, metadata=""):
        data = {
            'value': value,
            'metadata': metadata
        }

        return self.request('createValue', data)

    def findAllValues(self):
        return self.request('showValue', {})

    def findValueByValue(self, value):
        values = self.findAllValues()
        values = [x for x in values if x['label'] == value]
        if len(values) == 0:
            raise Exception("Unknown value")
        else:
            return values[0]

    def findValueById(self, id_number):
        values = self.findAllValues()
        values = [x for x in values if str(x['id']) == str(id_number)]
        if len(values) == 0:
            raise Exception("Unknown ID")
        else:
            return values[0]

    def updateValue(self, id_number, new_value, metadata=None):
        data = {
            'id': id_number,
            'new_value': new_value
        }

        if metadata is not None:
            data['metadata'] = metadata

        return self.request('updateValue', data)

    def deleteValue(self, id_number):
        data = {
            'id': id_number
        }

        return self.request('deleteValue', data)


class OrganismsClient(Client):
    CLIENT_BASE = '/organism/'

    def addOrganism(self, commonName, directory, blatdb=None, species=None,
                    genus=None, public=False):
        data = {
            'commonName': commonName,
            'directory': directory,
            'publicMode': public,
        }

        if blatdb is not None:
            data['blatdb'] = blatdb
        if genus is not None:
            data['genus'] = genus
        if species is not None:
            data['species'] = species

        return self.request('addOrganism', data)

    def findAllOrganisms(self):
        return self.request('findAllOrganisms', {})

    def findOrganismByCn(self, cn):
        orgs = self.findAllOrganisms()
        orgs = [x for x in orgs if x['commonName'] == cn]
        if len(orgs) == 0:
            raise Exception("Unknown common name")
        else:
            return orgs[0]

    def findOrganismById(self, id_number):
        orgs = self.findAllOrganisms()
        orgs = [x for x in orgs if str(x['id']) == str(id_number)]
        if len(orgs) == 0:
            raise Exception("Unknown ID")
        else:
            return orgs[0]

    def deleteOrganism(self, organismId):
        return self.request('deleteOrganism', {'id': organismId})

    def deleteOrganismFeatures(self, organismId):
        return self.request('deleteOrganismFeatures', {'id': organismId})

    def getSequencesForOrganism(self, commonName):
        return self.request('getSequencesForOrganism', {'organism': commonName})

    def updateOrganismInfo(self, organismId, commonName, directory, blatdb=None, species=None, genus=None, public=False):
        data = {
            'id': organismId,
            'name': commonName,
            'directory': directory,
            'publicMode': public,
        }

        if blatdb is not None:
            data['blatdb'] = blatdb
        if genus is not None:
            data['genus'] = genus
        if species is not None:
            data['species'] = species

        return self.request('updateOrganismInfo', data)


class UsersClient(Client):
    CLIENT_BASE = '/user/'

    # Real one
    # def getOrganismPermissionsForUser(self, user):
    # data = {
    # 'userId': user.userId,
    # }
    # return self.request('getOrganismPermissionsForUser', data)

    # Utter frigging hack
    def getOrganismPermissionsForUser(self, user):
        return self.loadUser(user).organismPermissions

    def updateOrganismPermission(self, user, organism, administrate=False,
                                 write=False, export=False, read=False):
        data = {
            'userId': user.userId,
            'organism': organism,
            'ADMINISTRATE': administrate,
            'WRITE': write,
            'EXPORT': export,
            'READ': read,
        }
        return self.request('updateOrganismPermission', data)

    def loadUser(self, user):
        return self.loadUserById(user.userId)

    def loadUserById(self, userId):
        res = self.request('loadUsers', {'userId': userId})
        if isinstance(res, list):
            # We can only match one, right?
            return UserObj(**res[0])
        else:
            return res

    def loadUsers(self, email=None):
        res = self.request('loadUsers', {})
        data = [UserObj(**x) for x in res]
        if email is not None:
            data = [x for x in data if x.username == email]

        return data

    def addUserToGroup(self, group, user):
        data = {'group': group.name, 'userId': user.userId}
        return self.request('addUserToGroup', data)

    def removeUserFromGroup(self, group, user):
        data = {'group': group.name, 'userId': user.userId}
        return self.request('removeUserFromGroup', data)

    def createUser(self, email, firstName, lastName, newPassword, role="user", groups=None):
        data = {
            'firstName': firstName,
            'lastName': lastName,
            'email': email,
            'role': role,
            'groups': [] if groups is None else groups,
            # 'availableGroups': [],
            'newPassword': newPassword,
            # 'organismPermissions': [],
        }
        return self.request('createUser', data)

    def deleteUser(self, user):
        return self.request('deleteUser', {'userId': user.userId})

    def updateUser(self, user, email, firstName, lastName, newPassword):
        data = {
            'userId': user.userId,
            'email': email,
            'firstName': firstName,
            'lastName': lastName,
            'newPassword': newPassword,
        }
        return self.request('updateUser', data)


class RemoteRecord(Client):
    CLIENT_BASE = None

    def ParseRecord(self, cn):
        org = self._wa.organisms.findOrganismByCn(cn)
        self._wa.annotations.setSequence(org['commonName'], org['id'])

        data = io.StringIO(self._wa.io.write(
            exportType='GFF3',
            seqType='genomic',
            exportAllSequences=False,
            exportGff3Fasta=True,
            output="text",
            exportFormat="text",
            sequences=cn,
        ))
        data.seek(0)

        for record in GFF.parse(data):
            yield WebApolloSeqRecord(record, self._wa)


class WebApolloSeqRecord(object):
    def __init__(self, sr, wa):
        self._sr = sr
        self._wa = wa

    def __dir__(self):
        return dir(self._sr)

    def __getattr__(self, key):
        if key in ('_sr', '_wa'):
            return self.__dict__[key]
        else:
            if key == 'features':
                return (WebApolloSeqFeature(x, self._wa)
                        for x in self._sr.__dict__[key])
            else:
                return self._sr.__dict__[key]

    def __setattr__(self, key, value):
        if key in ('_sd', '_wa'):
            self.__dict__[key] = value
        else:
            self._sr.__dict__[key] = value
            # Methods acting on the SeqRecord object


class WebApolloSeqFeature(object):
    def __init__(self, sf, wa):
        self._sf = sf
        self._wa = wa

    def __dir__(self):
        return dir(self._sf)

    def __getattr__(self, key):
        if key in ('_sf', '_wa'):
            return self.__dict__[key]
        else:
            return self._sf.__dict__[key]

    def __setattr__(self, key, value):
        if key in ('_sf', '_wa'):
            self.__dict__[key] = value
        else:
            # Methods acting on the SeqFeature object
            if key == 'location':
                if value.strand != self._sf.location.strand:
                    self.wa.annotations.flipStrand(
                        self._sf.qualifiers['ID'][0]
                    )

                self.wa.annotations.setBoundaries(
                    self._sf.qualifiers['ID'][0],
                    value.start,
                    value.end,
                )

                self._sf.__dict__[key] = value
            else:
                self._sf.__dict__[key] = value


def _tnType(feature):
    if feature.type in ('gene', 'mRNA', 'exon', 'CDS', 'terminator', 'tRNA'):
        return feature.type
    else:
        return 'exon'


def _yieldFeatData(features):
    for f in features:
        current = {
            'location': {
                'strand': f.strand,
                'fmin': int(f.location.start),
                'fmax': int(f.location.end),
            },
            'type': {
                'name': _tnType(f),
                'cv': {
                    'name': 'sequence',
                }
            },
        }
        if f.type in ('gene', 'mRNA'):
            current['name'] = f.qualifiers.get('Name', [f.id])[0]
        if hasattr(f, 'sub_features') and len(f.sub_features) > 0:
            current['children'] = [x for x in _yieldFeatData(f.sub_features)]

        yield current


def featuresToFeatureSchema(features):
    compiled = []
    for feature in features:
        # if feature.type != 'gene':
            # log.warn("Not able to handle %s features just yet...", feature.type)
            # continue

        for x in _yieldFeatData([feature]):
            compiled.append(x)
    return compiled


def accessible_organisms(user, orgs):
    permissionMap = {
        x['organism']: x['permissions']
        for x in user.organismPermissions
        if 'WRITE' in x['permissions'] or
        'READ' in x['permissions'] or
        'ADMINISTRATE' in x['permissions'] or
        user.role == 'ADMIN'
    }

    if 'error' in orgs:
        raise Exception("Error received from Apollo server: \"%s\"" % orgs['error'])

    return [
        (org['commonName'], org['id'], False)
        for org in sorted(orgs, key=lambda x: x['commonName'])
        if org['commonName'] in permissionMap
    ]


def galaxy_list_groups(trans, *args, **kwargs):
    email = trans.get_user().email
    wa = WebApolloInstance(
        os.environ['GALAXY_WEBAPOLLO_URL'],
        os.environ['GALAXY_WEBAPOLLO_USER'],
        os.environ['GALAXY_WEBAPOLLO_PASSWORD']
    )
    # Assert that the email exists in apollo
    try:
        gx_user = wa.requireUser(email)
    except UnknownUserException:
        return []

    # Key for cached data
    cacheKey = 'groups-' + email
    # We don't want to trust "if key in cache" because between asking and fetch
    # it might through key error.
    if cacheKey not in cache:
        # However if it ISN'T there, we know we're safe to fetch + put in
        # there.
        data = _galaxy_list_groups(wa, gx_user, *args, **kwargs)
        cache[cacheKey] = data
        return data
    try:
        # The cache key may or may not be in the cache at this point, it
        # /likely/ is. However we take no chances that it wasn't evicted between
        # when we checked above and now, so we reference the object from the
        # cache in preparation to return.
        data = cache[cacheKey]
        return data
    except KeyError:
        # If access fails due to eviction, we will fail over and can ensure that
        # data is inserted.
        data = _galaxy_list_groups(wa, gx_user, *args, **kwargs)
        cache[cacheKey] = data
        return data


def _galaxy_list_groups(wa, gx_user, *args, **kwargs):
    # Fetch the groups.
    group_data = []
    for group in wa.groups.loadGroups():
        # Reformat
        group_data.append((group.name, group.groupId, False))
    return group_data


def galaxy_list_orgs(trans, *args, **kwargs):
    email = trans.get_user().email
    wa = WebApolloInstance(
        os.environ['GALAXY_WEBAPOLLO_URL'],
        os.environ['GALAXY_WEBAPOLLO_USER'],
        os.environ['GALAXY_WEBAPOLLO_PASSWORD']
    )
    try:
        gx_user = wa.requireUser(email)
    except UnknownUserException:
        return []

    # Key for cached data
    cacheKey = 'orgs-' + email
    if cacheKey not in cache:
        data = _galaxy_list_orgs(wa, gx_user, *args, **kwargs)
        cache[cacheKey] = data
        return data
    try:
        data = cache[cacheKey]
        return data
    except KeyError:
        data = _galaxy_list_orgs(wa, gx_user, *args, **kwargs)
        cache[cacheKey] = data
        return data


def _galaxy_list_orgs(wa, gx_user, *args, **kwargs):
    # Fetch all organisms
    all_orgs = wa.organisms.findAllOrganisms()
    # Figure out which are accessible to the user
    orgs = accessible_organisms(gx_user, all_orgs)
    # Return org list
    return orgs


# This is all for implementing the command line interface for testing.
class obj(object):
    pass


class fakeTrans(object):

    def __init__(self, username):
        self.un = username

    def get_user(self):
        o = obj()
        o.email = self.un
        return o

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test access to apollo server')
    parser.add_argument('email', help='Email of user to test')
    parser.add_argument('--action', choices=['org', 'group'], default='org', help='Data set to test, fetch a list of groups or users known to the requesting user.')
    args = parser.parse_args()

    trans = fakeTrans(args.email)
    if args.action == 'org':
        for f in galaxy_list_orgs(trans):
            print(f)
    else:
        for f in galaxy_list_groups(trans):
            print(f)
