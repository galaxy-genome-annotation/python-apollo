import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('addValue')
@click.argument("value")

@click.option(
    "--metadata",
    help=""
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, value, metadata=""):
    """Warning: Undocumented Method
    """
    return ctx.gi.cannedvalues.addValue(value, metadata=metadata)
