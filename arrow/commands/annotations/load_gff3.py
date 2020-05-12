import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, str_output


@click.command('load_gff3')
@click.argument("organism", type=str)
@click.argument("gff3", type=str)
@click.option(
    "--source",
    help="URL where the input dataset can be found.",
    type=str
)
@click.option(
    "--test",
    is_flag=True,
    help="Run as a test without writing.",
)
@pass_context
@custom_exception
@str_output
def cli(ctx, organism, gff3, source="", test=False):
    """Load a full GFF3 into annotation track

Output:

    Loading report
    """
    return ctx.gi.annotations.load_gff3(organism, gff3, source=source,test=test)
