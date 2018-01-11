import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, list_output


@click.command('get_comments')
@pass_context
@custom_exception
@list_output
def cli(ctx):
    """Get all canned comments available in this Apollo instance

Output:

    list of canned comment info dictionaries
    """
    return ctx.gi.cannedcomments.get_comments()
