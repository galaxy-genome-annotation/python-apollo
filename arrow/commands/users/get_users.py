import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, list_output, _arg_split

@click.command('get_users')


@pass_context
@custom_exception
@list_output
def cli(ctx):
    """Get all users known to this Apollo instance

Output:

     list of user info dictionaries
        
    """
    return ctx.gi.users.get_users()
