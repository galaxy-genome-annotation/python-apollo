import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, list_output


@click.command('get_group_admin')
@click.argument("group", type=str)
@pass_context
@custom_exception
@list_output
def cli(ctx, group):
    """Get the group's admins

Output:

    a list containing group admins
    """
    return ctx.gi.groups.get_group_admin(group)
