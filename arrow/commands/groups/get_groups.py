import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, list_output

@click.command('get_groups')


@pass_context
@apollo_exception
@list_output
def cli(ctx):
    """Get all the groups

Output:

     list of a dictionaries containing group information
        
    """
    return ctx.gi.groups.get_groups()
