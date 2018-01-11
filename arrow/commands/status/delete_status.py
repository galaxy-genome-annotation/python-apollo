import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('delete_status')
@click.argument("id_number", type=int)
@pass_context
@custom_exception
@dict_output
def cli(ctx, id_number):
    """Delete a status

Output:

    an empty dictionary
    """
    return ctx.gi.status.delete_status(id_number)
