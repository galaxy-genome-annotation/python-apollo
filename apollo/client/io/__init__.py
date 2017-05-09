"""
Contains possible interactions with the Apollo IO Module
"""
from apollo.client import Client


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

