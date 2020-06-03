import argparse
import json
import logging
import time

from Bio import SeqIO

from apollo.exceptions import UnknownUserException

log = logging.getLogger()

gene_types = ["gene"]
coding_transcript_types = ["mRNA"]
pseudogenes_types = ["pseudogene", "pseudogenic_region", "processed_pseudogene"]
noncoding_transcript_types = ['transcript', 'tRNA', 'snRNA', 'snoRNA', 'ncRNA', 'rRNA', 'mRNA', 'miRNA', 'guide_RNA',
                              'RNase_P_RNA', 'telomerase_RNA', 'SRP_RNA', 'lnc_RNA', 'RNase_MRP_RNA', 'scRNA', 'piRNA',
                              'tmRNA', 'enzymatic_RNA']
single_level_feature_types = ["repeat_region", "terminator", "shine_dalgarno_sequence", "transposable_element"]


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
        all_orgs = wa.organisms.get_organisms()
        if 'error' in all_orgs:
            raise Exception("Error while getting the list of organisms: %s" % all_orgs)
        orgs = [org['commonName'] for org in all_orgs if str(args.org_id) == str(org['id'])]
        return orgs
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


def _yieldFeatData(features, use_name=False, disable_cds_recalculation=False):
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
        if disable_cds_recalculation is True:
            current['use_cds'] = 'true'

        if f.type in (coding_transcript_types + noncoding_transcript_types + gene_types + pseudogenes_types
                      + single_level_feature_types):
            current['name'] = f.qualifiers.get('Name', [f.id])[0]

        if use_name is True:
            current['use_name'] = True

        # if OGS:
        # TODO: handle comments
        # TODO: handle dbxrefs
        # TODO: handle attributes
        # TODO: handle aliases
        # TODO: handle description
        # TODO: handle GO, Gene Product, Provenance

        if hasattr(f, 'sub_features') and len(f.sub_features) > 0:
            current['children'] = [x for x in _yieldFeatData(f.sub_features)]

        yield current


def add_property_to_feature(feature, property_key, property_value):
    """

    :param feature:
    :type property_key: str
    :param property_key:
    :type property_value: str
    :param property_value:
    :return:
    """
    if "feature_property" not in feature:
        feature["feature_property"] = {}
    feature["feature_property"][property_key] = property_value
    return feature


def features_to_feature_schema(features, use_name=False, disable_cds_recalculation=False):
    """

    :param disable_cds_recalculation:
    :param use_name:
    :param features:
    :return:
    """
    compiled = []
    for feature in features:
        for x in _yieldFeatData([feature], use_name, disable_cds_recalculation):
            compiled.append(x)
    return compiled


def retry(closure, sleep=1, limit=5):
    """
    Apollo has the bad habit of returning 500 errors if you call APIs
    too quickly, largely because of the unholy things that happen in
    grails.

    To deal with the fact that we cannot send an addComments call too
    quickly after a createFeature call, we have this function that will
    keep calling a closure until it works.
    """
    count = 0
    while True:
        count += 1

        if count >= limit:
            return False
        try:
            # Try calling it
            closure()
            # If successful, exit
            return True
        except Exception as e:
            log.info(str(e)[0:100])
            time.sleep(sleep)
