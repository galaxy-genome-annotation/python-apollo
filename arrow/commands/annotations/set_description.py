import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('set_description')
@click.argument("feature_id", type=str)
@click.argument("description", type=str)
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
def cli(ctx, feature_id, description, organism="", sequence=""):
    """Set a feature's description

Output:

    A standard apollo feature dictionary ({"features": [{...}]})
    """
    return ctx.gi.annotations.set_description(feature_id, description, organism=organism, sequence=sequence)
