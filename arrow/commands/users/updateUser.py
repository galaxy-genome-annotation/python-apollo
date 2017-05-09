import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

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
