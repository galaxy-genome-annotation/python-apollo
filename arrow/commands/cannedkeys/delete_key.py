import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('delete_key')
@click.argument("id_number", type=int)
@pass_context
@custom_exception
@dict_output
def cli(ctx, id_number):
    """Update a canned key

Output:

    an empty dictionary
    """
    return ctx.gi.cannedkeys.delete_key(id_number)
