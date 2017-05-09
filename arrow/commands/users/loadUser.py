import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('loadUser')
@click.argument("user")


@pass_context
@apollo_exception
@dict_output
def cli(ctx, user):
    """Warning: Undocumented Method
    """
    return ctx.gi.users.loadUser(user)
