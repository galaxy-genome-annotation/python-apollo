import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('set_name')
@click.argument("feature_id", type=str)
@click.argument("name", type=str)
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
def cli(ctx, feature_id, name, organism="", sequence=""):
    """Set a feature's name

Output:

    A standard apollo feature dictionary ({"features": [{...}]})
    """
    return ctx.gi.annotations.set_name(feature_id, name, organism=organism, sequence=sequence)
