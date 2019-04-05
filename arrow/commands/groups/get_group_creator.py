import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, list_output


@click.command('get_group_creator')
@click.argument("group", type=str)
@pass_context
@custom_exception
@list_output
def cli(ctx, group):
    """Get the group's creator

Output:

    creator userId
    """
    return ctx.gi.groups.get_group_creator(group)
