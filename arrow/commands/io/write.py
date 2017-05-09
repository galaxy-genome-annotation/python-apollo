import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('write')

@click.option(
    "--exportType",
    help=""
)
@click.option(
    "--seqType",
    help=""
)
@click.option(
    "--exportFormat",
    help=""
)
@click.option(
    "--sequences",
    help=""
)
@click.option(
    "--organism",
    help=""
)
@click.option(
    "--output",
    help=""
)
@click.option(
    "--exportAllSequences",
    help=""
)
@click.option(
    "--exportGff3Fasta",
    help=""
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, exportType="", seqType="", exportFormat="", sequences="", organism="", output="", exportAllSequences=False, exportGff3Fasta=False):
    """Warning: Undocumented Method
    """
    return ctx.gi.io.write(exportType=exportType, seqType=seqType, exportFormat=exportFormat, sequences=sequences, organism=organism, output=output, exportAllSequences=exportAllSequences, exportGff3Fasta=exportGff3Fasta)
