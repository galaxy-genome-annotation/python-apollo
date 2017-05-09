import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('get_users')


@pass_context
@apollo_exception
@dict_output
def cli(ctx):
    """Get all users known to this Apollo instance
    """
    return ctx.gi.users.get_users()
