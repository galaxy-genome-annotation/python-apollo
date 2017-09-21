import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('add_comment')
@click.argument("feature_id", type=str)
@click.option(
    "--comments",
    help="Feature comments",
    type=str,
    multiple=True
)
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
def cli(ctx, feature_id, comments=None, organism="", sequence=""):
    """Set a feature's description

Output:

    A standard apollo feature dictionary ({"features": [{...}]})
    """
    return ctx.gi.annotations.add_comment(feature_id, comments=comments, organism=organism, sequence=sequence)
