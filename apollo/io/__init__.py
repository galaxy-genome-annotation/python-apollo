"""
Contains possible interactions with the Apollo IO Module
"""
from apollo.client import Client


class IOClient(Client):
    CLIENT_BASE = '/IOService/'

    def write_downloadable(self, organism, export_type='FASTA',
                           seq_type='peptide', export_format='text',
                           export_gff3_fasta=False, sequences=[], region=None):
        """
        Prepare a download for an organism

        :type organism: str
        :param organism: organism common name

        :type sequences: str
        :param sequences: Names of references sequences to add (default is all)

        :type export_type: str
        :param export_type: Export type. Choices: FASTA, GFF3, VCF

        :type seq_type: str
        :param seq_type: Export selection. Choices: peptide, cds, cdna, genomic

        :type export_format: str
        :param export_format: Export format, either gzip or text

        :type export_gff3_fasta: bool
        :param export_gff3_fasta: Export reference sequence when exporting GFF3 annotations.

        :type region: str
        :param region: Region to export in form sequence:min..max e.g., chr3:1001..1034

        :rtype: dict
        :return: a dictionary containing download information
        """

        if export_format.lower() not in ('gzip', 'text'):
            raise Exception("export_format must be one of file, text")

        if export_type.lower() not in ('fasta', 'gff3', 'vcf'):
            raise Exception("export_type must be one of FASTA, GFF3, VCF")

        data = {
            'type': export_type,
            'seq_type': seq_type,
            'format': export_format,
            'sequences': sequences,
            'organism': organism,
            'output': 'file',
            'exportAllSequences': True if not sequences else len(sequences) == 0,
            'exportGff3Fasta': export_gff3_fasta,
        }

        if region:
            data['region'] = region

        return self.post('write', data)

    def write_text(self, organism, export_type='FASTA', seq_type='peptide',
                   export_format='text', export_gff3_fasta=False,
                   sequences=[], region=None):
        """
        [DEPRECATED, use write_downloadable] Download or prepare a download for an organism

        :type organism: str
        :param organism: organism common name

        :type sequences: str
        :param sequences: Names of references sequences to add (default is all)

        :type export_type: str
        :param export_type: Export type. Choices: FASTA, GFF3, VCF

        :type seq_type: str
        :param seq_type: Export selection. Choices: peptide, cds, cdna, genomic

        :type export_format: str
        :param export_format: Export format, either gzip or text

        :type export_gff3_fasta: bool
        :param export_gff3_fasta: Export reference sequence when exporting GFF3 annotations.

        :type region: str
        :param region: Region to export in form sequence:min..max e.g., chr3:1001..1034

        :rtype: str
        :return: the exported data
        """

        return self.write_downloadable(organism, export_type, seq_type,
                                       export_format, export_gff3_fasta,
                                       sequences, region)

    def download(self, uuid, output_format='gzip'):
        """
        Download pre-prepared data by UUID

        :type uuid: str
        :param uuid: Data UUID

        :type output_format: str
        :param output_format: Output format of the data, either "gzip" or "text"

        :rtype: str
        :return: The downloaded content
        """

        if output_format.lower() not in ('gzip', 'text'):
            raise Exception("output_format must be one of file, text")

        data = {
            'format': output_format,
            'uuid': uuid,
        }
        return self.get('download', get_params=data, is_json=False)
