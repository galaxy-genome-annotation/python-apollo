import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('set_translation_end')
@click.argument("feature_id", type=str)
@click.argument("end", type=int)
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
def cli(ctx, feature_id, end, organism="", sequence=""):
    """Set a feature's end

Output:

    A standard apollo feature dictionary ({"features": [{...}]})
    """
    return ctx.gi.annotations.set_translation_end(feature_id, end, organism=organism, sequence=sequence)
