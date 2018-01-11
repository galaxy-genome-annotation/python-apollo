import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('add_feature')
@click.option(
    "--feature",
    help="Feature information",
    type=str
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
def cli(ctx, feature={}, organism="", sequence=""):
    """Add a feature

Output:

    A standard apollo feature dictionary ({"features": [{...}]})
    """
    return ctx.gi.annotations.add_feature(feature=feature, organism=organism, sequence=sequence)
