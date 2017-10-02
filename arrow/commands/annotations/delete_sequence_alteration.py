import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, list_output


@click.command('delete_sequence_alteration')
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
@list_output
def cli(ctx, feature_id, organism="", sequence=""):
    """[UNTESTED] Delete a specific feature alteration

Output:

    A list of sequence alterations(?)
    """
    return ctx.gi.annotations.delete_sequence_alteration(feature_id, organism=organism, sequence=sequence)
