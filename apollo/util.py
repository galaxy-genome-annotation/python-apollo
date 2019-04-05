import argparse
import json
from Bio import SeqIO
from apollo.exceptions import UnknownUserException


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
        #     log.warn("Not able to handle %s features just yet...", feature.type)
        #     continue

        for x in _yieldFeatData([feature]):
            compiled.append(x)
    return compiled
