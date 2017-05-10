import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output, _arg_split

@click.command('update_membership')
@click.argument("group_id", type=int)

@click.option(
    "--users",
    help="List of emails",
    type=str,
    callback=_arg_split
)

@pass_context
@apollo_exception
@dict_output
def cli(ctx, group_id, users=None):
    """Update the group's membership

Output:

     dictionary of group information
        
    """
    return ctx.gi.groups.update_membership(group_id, users=users)
