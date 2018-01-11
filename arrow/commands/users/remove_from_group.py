import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('remove_from_group')
@click.argument("group", type=str)
@click.argument("user", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, group, user):
    """Remove a user from a group

Output:

    an empty dictionary
    """
    return ctx.gi.users.remove_from_group(group, user)
