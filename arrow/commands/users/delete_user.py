import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('delete_user')
@click.argument("user", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, user):
    """Delete a user

Output:

    an empty dictionary
    """
    return ctx.gi.users.delete_user(user)
