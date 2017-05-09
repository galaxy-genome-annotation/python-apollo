import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('write')
@click.argument("organism", type=str)

@click.option(
    "--sequences",
    help="Names of references sequences to add (default is all)",
    type=str
)
@click.option(
    "--export_type",
    help="Export type. Choices: FASTA, GFF3",
    type=str
)
@click.option(
    "--seq_type",
    help="Export selection. Choices: peptide, cds, cdna, genomic",
    type=str
)
@click.option(
    "--export_format",
    help="Export format, either gzip or text",
    type=str
)
@click.option(
    "--output",
    help="Export destination, either file or \"text\" (i.e. response)",
    type=str
)
@click.option(
    "--export_gff3_fasta",
    help="Export reference sequence when exporting GFF3 annotations.",
    is_flag=True
)

@pass_context
@apollo_exception
@dict_output
def cli(ctx, organism, sequences=None, export_type="FASTA", seq_type="peptide", export_format="text", output="text", export_gff3_fasta=False):
    """Download or prepare a download for an organism
    """
    return ctx.gi.io.write(organism, sequences=sequences, export_type=export_type, seq_type=seq_type, export_format=export_format, output=output, export_gff3_fasta=export_gff3_fasta)
