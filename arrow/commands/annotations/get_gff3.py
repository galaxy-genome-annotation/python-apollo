import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, str_output


@click.command('get_gff3')
@click.argument("feature_id", type=str)
@click.option(
    "--organism",
    help="Organism Common Name",
    type=str
)
@click.option(
    "--sequence",
    help="Sequence Name",
    type=str
)
@pass_context
@custom_exception
@str_output
def cli(ctx, feature_id, organism="", sequence=""):
    """Get the GFF3 associated with a feature

Output:

    GFF3 text content
    """
    return ctx.gi.annotations.get_gff3(feature_id, organism=organism, sequence=sequence)
