import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('delete_comment')
@click.argument("id_number", type=int)
@pass_context
@custom_exception
@dict_output
def cli(ctx, id_number):
    """Update a canned comment

Output:

    an empty dictionary
    """
    return ctx.gi.cannedcomments.delete_comment(id_number)
