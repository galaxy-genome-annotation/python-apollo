import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('activate_user')
@click.argument("user", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, user):
    """Activate a user

Output:

    an empty dictionary
    """
    return ctx.gi.users.activate_user(user)
