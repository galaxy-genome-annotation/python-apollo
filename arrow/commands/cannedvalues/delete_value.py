import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('delete_value')
@click.argument("id_number", type=int)
@pass_context
@custom_exception
@dict_output
def cli(ctx, id_number):
    """Update a canned value

Output:

    an empty dictionary
    """
    return ctx.gi.cannedvalues.delete_value(id_number)
