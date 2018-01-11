import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('create_user')
@click.argument("email", type=str)
@click.argument("first_name", type=str)
@click.argument("last_name", type=str)
@click.argument("password", type=str)
@click.option(
    "--role",
    help="User's default role, one of \"admin\" or \"user\"",
    default="user",
    show_default=True,
    type=str
)
@click.option(
    "--metadata",
    help="User metadata",
    type=str
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, email, first_name, last_name, password, role="user", metadata={}):
    """Create a new user

Output:

    an empty dictionary
    """
    return ctx.gi.users.create_user(email, first_name, last_name, password, role=role, metadata=metadata)
