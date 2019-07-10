import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, dict_output


@click.command('update_membership')
@click.option(
    "--group_id",
    help="Group ID Number",
    type=int
)
@click.option(
    "--users",
    help="List of emails",
    type=str,
    multiple=True
)
@click.option(
    "--memberships",
    help="Bulk memberships to update of the form: [ {groupId: <groupId>,users: [\"user1\", \"user2\", \"user3\"]}, {groupId:<another-groupId>, users: [\"user2\", \"user8\"]} (users and groupId will be ignored)",
    type=str,
    multiple=True
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, group_id="", users=None, memberships=None):
    """Update the group's membership

Output:

    dictionary of group information
    """
    return ctx.gi.groups.update_membership(group_id=group_id, users=users, memberships=memberships)
