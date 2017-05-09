import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('deleteKey')
@click.argument("id_number")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, id_number):
    """Warning: Undocumented Method
    """
    return ctx.gi.cannedkeys.deleteKey(id_number)
