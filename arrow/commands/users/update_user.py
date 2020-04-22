import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, dict_output


@click.command('update_user')
@click.argument("email", type=str)
@click.argument("first_name", type=str)
@click.argument("last_name", type=str)
@click.option(
    "--password",
    help="User's password (omit to keep untouched)",
    type=str
)
@click.option(
    "--metadata",
    help="User metadata",
    type=str
)
@click.option(
    "--new_email",
    help="User's new email (if you want to change it)",
    type=str
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, email, first_name, last_name, password="", metadata={}, new_email=""):
    """Update an existing user

Output:

    a dictionary containing user information
    """
    return ctx.gi.users.update_user(email, first_name, last_name, password=password, metadata=metadata, new_email=new_email)
