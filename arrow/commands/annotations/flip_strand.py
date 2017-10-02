import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('flip_strand')
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
    """Flip the strand of a feature

Output:

    A standard apollo feature dictionary ({"features": [{...}]})
    """
    return ctx.gi.annotations.flip_strand(feature_id, organism=organism, sequence=sequence)
