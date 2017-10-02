import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('update_group')
@click.argument("group_id", type=int)
@click.argument("new_name", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, group_id, new_name):
    """Update the name of a group

Output:

    a dictionary containing group information
    """
    return ctx.gi.groups.update_group(group_id, new_name)
