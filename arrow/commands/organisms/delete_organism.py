import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, list_output


@click.command('delete_organism')
@click.argument("organism_id", type=str)
@click.option(
    "--suppress_output",
    help="Suppress return of all organisms (true / false) (default false)",
    is_flag=True
)
@pass_context
@custom_exception
@list_output
def cli(ctx, organism_id, suppress_output=False):
    """Delete an organism

Output:

    A list of all remaining organisms
    """
    return ctx.gi.organisms.delete_organism(organism_id, suppress_output=suppress_output)
