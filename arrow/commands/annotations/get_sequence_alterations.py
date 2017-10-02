import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, list_output


@click.command('get_sequence_alterations')
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
def cli(ctx, organism="", sequence=""):
    """[UNTESTED] Get all of the sequence's alterations

Output:

    A list of sequence alterations(?)
    """
    return ctx.gi.annotations.get_sequence_alterations(organism=organism, sequence=sequence)
