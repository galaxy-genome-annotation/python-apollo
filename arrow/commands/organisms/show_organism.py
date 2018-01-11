import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('show_organism')
@click.argument("common_name", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, common_name):
    """Get information about a specific organism.

Output:

    a dictionary containing the organism's information
    """
    return ctx.gi.organisms.show_organism(common_name)
