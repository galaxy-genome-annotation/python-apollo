import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, dict_output, _arg_split

@click.command('show_group')
@click.argument("group_id")

@click.option(
    "--group",
    help="Group ID Number",
    type=int
)

@pass_context
@custom_exception
@dict_output
def cli(ctx, group_id, group=None):
    """Get information about a group

Output:

     a dictionary containing group information
        
    """
    kwargs = {}

    return ctx.gi.groups.show_group(group_id, **kwargs)
