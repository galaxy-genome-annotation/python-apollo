import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, str_output


@click.command('write_text')
@click.argument("organism", type=str)
@click.option(
    "--export_type",
    help="Export type. Choices: FASTA, GFF3, VCF",
    default="FASTA",
    show_default=True,
    type=str
)
@click.option(
    "--seq_type",
    help="Export selection. Choices: peptide, cds, cdna, genomic",
    default="peptide",
    show_default=True,
    type=str
)
@click.option(
    "--export_format",
    help="Export format, either gzip or text",
    default="text",
    show_default=True,
    type=str
)
@click.option(
    "--export_gff3_fasta",
    help="Export reference sequence when exporting GFF3 annotations.",
    is_flag=True
)
@click.option(
    "--sequences",
    help="Names of references sequences to add (default is all)",
    type=str
)
@click.option(
    "--region",
    help="Region to export in form sequence:min..max e.g., chr3:1001..1034",
    type=str
)
@pass_context
@custom_exception
@str_output
def cli(ctx, organism, export_type="FASTA", seq_type="peptide", export_format="text", export_gff3_fasta=False, sequences=None, region=""):
    """[DEPRECATED, use write_downloadable] Download or prepare a download for an organism

Output:

    the exported data
    """
    return ctx.gi.io.write_text(organism, export_type=export_type, seq_type=seq_type, export_format=export_format, export_gff3_fasta=export_gff3_fasta, sequences=sequences, region=region)
