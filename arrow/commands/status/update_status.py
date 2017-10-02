import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('update_status')
@click.argument("id_number", type=int)
@click.argument("new_value", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, id_number, new_value):
    """Update a status name

Output:

    an empty dictionary
    """
    return ctx.gi.status.update_status(id_number, new_value)
