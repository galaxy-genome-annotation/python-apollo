import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('get_organism_creator')
@click.argument("organism_id", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, organism_id):
    """Get the creator of an organism

Output:

    a dictionary containing user information
    """
    return ctx.gi.organisms.get_organism_creator(organism_id)
