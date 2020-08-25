import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, list_output


@click.command('delete_organism')
@click.argument("organism_id", type=str)
@click.option(
    "--return_no_organisms",
    help="Return no organisms from command",
    is_flag=True
)
@pass_context
@custom_exception
@list_output
def cli(ctx, organism_id, return_no_organisms=False):
    """Delete an organism

Output:

    A list of all remaining organisms
    """
    return ctx.gi.organisms.delete_organism(organism_id, return_all=(return_no_organisms == False))
