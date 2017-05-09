import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('updateKey')
@click.argument("id_number")
@click.argument("new_key")

@click.option(
    "--metadata",
    help=""
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, id_number, new_key, metadata=""):
    """Warning: Undocumented Method
    """
    return ctx.gi.cannedkeys.updateKey(id_number, new_key, metadata=metadata)
