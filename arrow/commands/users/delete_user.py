import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output, _arg_split

@click.command('delete_user')
@click.argument("user", type=str)


@pass_context
@apollo_exception
@dict_output
def cli(ctx, user):
    """Delete a user

Output:

     an empty dictionary
        
    """
    return ctx.gi.users.delete_user(user)