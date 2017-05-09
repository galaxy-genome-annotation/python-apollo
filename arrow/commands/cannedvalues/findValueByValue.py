import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('findValueByValue')
@click.argument("value")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, value):
    """Warning: Undocumented Method
    """
    return ctx.gi.cannedvalues.findValueByValue(value)
