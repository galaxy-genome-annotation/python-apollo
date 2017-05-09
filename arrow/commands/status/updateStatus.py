import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('updateStatus')
@click.argument("id_number")
@click.argument("new_value")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, id_number, new_value):
    """Warning: Undocumented Method
    """
    return ctx.gi.status.updateStatus(id_number, new_value)
