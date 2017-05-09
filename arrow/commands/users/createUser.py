import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('createUser')
@click.argument("email")
@click.argument("firstName")
@click.argument("lastName")
@click.argument("newPassword")

@click.option(
    "--role",
    help=""
)
@click.option(
    "--groups",
    help=""
)

@pass_context
@apollo_exception
@dict_output
def cli(ctx, email, firstName, lastName, newPassword, role="", groups=""):
    """Warning: Undocumented Method
    """
    return ctx.gi.users.createUser(email, firstName, lastName, newPassword, role=role, groups=groups)
