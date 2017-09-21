import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('updateStatus')
@click.argument("id_number")
@click.argument("new_value")
@pass_context
@custom_exception
@dict_output
def cli(ctx, id_number, new_value):
    """TODO: Undocumented

Output:

    ???
    """
    return ctx.gi.status.updateStatus(id_number, new_value)
