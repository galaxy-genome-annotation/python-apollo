import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output, list_output, str_output

@click.command('remove_from_group')
@click.argument("group", type=str)
@click.argument("user", type=str)


@pass_context
@apollo_exception
@dict_output
def cli(ctx, group, user):
    """Remove a user from a group
    """
    return ctx.gi.users.remove_from_group(group, user)
