import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('addUserToGroup')
@click.argument("group")
@click.argument("user")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, group, user):
    """Warning: Undocumented Method
    """
    return ctx.gi.users.addUserToGroup(group, user)
