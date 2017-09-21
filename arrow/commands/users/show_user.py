import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('show_user')
@click.argument("user", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, user):
    """Get a specific user

Output:

    a dictionary containing user information
    """
    return ctx.gi.users.show_user(user)
