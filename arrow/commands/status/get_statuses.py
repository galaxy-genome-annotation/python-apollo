import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, list_output


@click.command('get_statuses')
@pass_context
@custom_exception
@list_output
def cli(ctx):
    """Get all statuses available in this Apollo instance

Output:

    list of status info dictionaries
    """
    return ctx.gi.status.get_statuses()
