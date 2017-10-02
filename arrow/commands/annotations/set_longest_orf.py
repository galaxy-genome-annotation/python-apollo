import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('set_longest_orf')
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
    """Automatically pick the longest ORF in a feature

Output:

    A standard apollo feature dictionary ({"features": [{...}]})
    """
    return ctx.gi.annotations.set_longest_orf(feature_id, organism=organism, sequence=sequence)
