import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, list_output


@click.command('get_users')
@click.option(
    "--omit_empty_organisms",
    help="Will omit users having no access to any organism",
    is_flag=True
)
@pass_context
@custom_exception
@list_output
def cli(ctx, omit_empty_organisms=False):
    """Get all users known to this Apollo instance

Output:

    list of user info dictionaries
    """
    return ctx.gi.users.get_users(omit_empty_organisms=omit_empty_organisms)
