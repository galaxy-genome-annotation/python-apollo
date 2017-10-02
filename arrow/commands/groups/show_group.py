import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('show_group')
@click.argument("group_id", type=int)
@pass_context
@custom_exception
@dict_output
def cli(ctx, group_id):
    """Get information about a group

Output:

    a dictionary containing group information
    """
    return ctx.gi.groups.show_group(group_id)
