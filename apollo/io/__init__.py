"""
Contains possible interactions with the Apollo IO Module
"""
from apollo.client import Client


class IOClient(Client):
    CLIENT_BASE = '/IOService/'

    def write(self, organism, sequences=[], export_type='FASTA',
              seq_type='peptide', export_format='text', output='text',
              export_gff3_fasta=False):
        """
        Download or prepare a download for an organism

        :type organism: str
        :param organism: organism common name

        :type sequences: str
        :param sequences: Names of references sequences to add (default is all)

        :type export_type: str
        :param export_type: Export type. Choices: FASTA, GFF3

        :type seq_type: str
        :param seq_type: Export selection. Choices: peptide, cds, cdna, genomic

        :type export_format: str
        :param export_format: Export format, either gzip or text

        :type output: str
        :param output: Export destination, either file or "text" (i.e. response)

        :type export_gff3_fasta: bool
        :param export_gff3_fasta: Export reference sequence when exporting GFF3 annotations.

        :rtype: dict
        :return: a dictionary containing user information
        """

        data = {
            'type': export_type,
            'seq_type': seq_type,
            'format': export_format,
            'sequences': sequences,
            'organism': organism,
            'output': output,
            'exportAllSequences': True if not sequences else len(sequences) == 0,
            'exportGff3Fasta': export_gff3_fasta,
        }

        return self.post('write', data, is_json=output == 'file')

    def download(self, uuid, output_format='gzip'):
        """
        Download pre-prepared data by UUID

        :type uuid: str
        :param uuid: Data UUID

        :type output_format: str
        :param output_format: Output format of the data, either "gzip" or "text"

        :rtype: dict
        :return: a dictionary
        """

        if output_format.lower() not in ('gzip', 'text'):
            raise Exception("outputFormat must be one of file, text")

        data = {
            'format': output_format,
            'uuid': uuid,
        }
        return self.post('write', data)
