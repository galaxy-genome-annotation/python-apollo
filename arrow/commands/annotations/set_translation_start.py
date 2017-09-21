import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('set_translation_start')
@click.argument("feature_id", type=str)
@click.argument("start", type=int)
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
def cli(ctx, feature_id, start, organism="", sequence=""):
    """Set the translation start of a feature

Output:

    A standard apollo feature dictionary ({"features": [{...}]})
    """
    return ctx.gi.annotations.set_translation_start(feature_id, start, organism=organism, sequence=sequence)
