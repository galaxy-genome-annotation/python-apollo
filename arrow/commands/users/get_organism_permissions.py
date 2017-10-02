import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('get_organism_permissions')
@click.argument("user", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, user):
    """Display a user's organism permissions

Output:

    a dictionary containing user's organism permissions
    """
    return ctx.gi.users.get_organism_permissions(user)
