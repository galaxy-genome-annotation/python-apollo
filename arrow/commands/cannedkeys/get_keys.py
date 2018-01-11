import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, list_output


@click.command('get_keys')
@pass_context
@custom_exception
@list_output
def cli(ctx):
    """Get all canned keys available in this Apollo instance

Output:

    list of canned key info dictionaries
    """
    return ctx.gi.cannedkeys.get_keys()
