import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('set_symbol')
@click.argument("feature_id", type=str)
@click.argument("symbol", type=str)
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
@dict_output
def cli(ctx, feature_id, symbol, organism="", sequence=""):
    """Set a feature's description

Output:

    A standard apollo feature dictionary ({"features": [{...}]})
    """
    return ctx.gi.annotations.set_symbol(feature_id, symbol, organism=organism, sequence=sequence)
