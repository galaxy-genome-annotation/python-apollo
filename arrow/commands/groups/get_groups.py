import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, list_output, _arg_split

@click.command('get_groups')


@pass_context
@custom_exception
@list_output
def cli(ctx):
    """Get all the groups

Output:

     list of a dictionaries containing group information
        
    """
    return ctx.gi.groups.get_groups()
