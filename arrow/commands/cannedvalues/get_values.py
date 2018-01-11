import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, list_output


@click.command('get_values')
@pass_context
@custom_exception
@list_output
def cli(ctx):
    """Get all canned values available in this Apollo instance

Output:

    list of canned value info dictionaries
    """
    return ctx.gi.cannedvalues.get_values()
