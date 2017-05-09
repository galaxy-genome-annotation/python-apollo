import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('deleteUser')
@click.argument("user")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, user):
    """Warning: Undocumented Method
    """
    return ctx.gi.users.deleteUser(user)
