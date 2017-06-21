import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, dict_output, _arg_split

@click.command('update_group')
@click.argument("group_id")
@click.argument("new_name", type=str)

@click.option(
    "--group",
    help="group ID number",
    type=int
)

@pass_context
@custom_exception
@dict_output
def cli(ctx, group_id, new_name, group=None):
    """Update the name of a group

Output:

     a dictionary containing group information
        
    """
    kwargs = {}

    return ctx.gi.groups.update_group(group_id, new_name, **kwargs)
