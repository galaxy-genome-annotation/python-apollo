import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('get_features')
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
def cli(ctx, organism="", sequence=""):
    """Get the features for an organism / sequence

Output:

    A standard apollo feature dictionary ({"features": [{...}]})
    """
    return ctx.gi.annotations.get_features(organism=organism, sequence=sequence)
