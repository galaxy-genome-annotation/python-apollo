import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('get_comments')
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
@dict_output
def cli(ctx, feature_id, organism="", sequence=""):
    """Get a feature's comments

Output:

    A standard apollo feature dictionary ({"features": [{...}]})
    """
    return ctx.gi.annotations.get_comments(feature_id, organism=organism, sequence=sequence)
