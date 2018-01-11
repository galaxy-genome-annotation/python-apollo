import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('delete_group')
@click.argument("group", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, group):
    """Delete a group

Output:

    an empty dictionary
    """
    return ctx.gi.groups.delete_group(group)
