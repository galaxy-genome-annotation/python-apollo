import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('get_user_creator')
@click.argument("user", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, user):
    """Get the creator of a user

Output:

    a dictionary containing user information
    """
    return ctx.gi.users.get_user_creator(user)
