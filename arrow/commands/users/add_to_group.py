import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('add_to_group')
@click.argument("group", type=str)
@click.argument("user", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, group, user):
    """Add a user to a group

Output:

    an empty dictionary
    """
    return ctx.gi.users.add_to_group(group, user)
