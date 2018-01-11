import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, list_output


@click.command('delete_organism')
@click.argument("organism_id", type=str)
@pass_context
@custom_exception
@list_output
def cli(ctx, organism_id):
    """Delete an organim

Output:

    A list of all remaining organisms
    """
    return ctx.gi.organisms.delete_organism(organism_id)
