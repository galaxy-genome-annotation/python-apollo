import collections
import logging
import time
from abc import abstractmethod
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
