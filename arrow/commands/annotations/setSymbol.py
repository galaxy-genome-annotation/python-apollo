import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('setSymbol')
@click.argument("symbols")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, symbols):
    """Warning: Undocumented Method
    """
    return ctx.gi.annotations.setSymbol(symbols)
