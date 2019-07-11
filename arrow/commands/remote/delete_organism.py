import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, dict_output


@click.command('delete_organism')
@click.argument("organism_id", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, organism_id):
    """Remove an organism completely.

Output:

    a dictionary with information about the deleted organism
    """
    return ctx.gi.remote.delete_organism(organism_id)
