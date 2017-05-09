import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('updateUser')
@click.argument("user")
@click.argument("email")
@click.argument("firstName")
@click.argument("lastName")
@click.argument("newPassword")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, user, email, firstName, lastName, newPassword):
    """Warning: Undocumented Method
    """
    return ctx.gi.users.updateUser(user, email, firstName, lastName, newPassword)
