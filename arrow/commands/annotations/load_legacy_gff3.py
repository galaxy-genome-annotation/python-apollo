import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, str_output


@click.command('load_legacy_gff3')
@click.argument("organism", type=str)
@click.argument("gff3", type=str)
@click.option(
    "--source",
    help="URL where the input dataset can be found.",
    type=str
)
@pass_context
@custom_exception
@str_output
def cli(ctx, organism, gff3, source=""):
    """Load a full GFF3 into annotation track (legacy version, kept for compatibility only)

Output:

    Loading report
    """
    return ctx.gi.annotations.load_legacy_gff3(organism, gff3, source=source)
