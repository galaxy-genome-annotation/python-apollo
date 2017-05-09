import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('setSymbol')
@click.argument("symbols")


@pass_context
@apollo_exception
@dict_output
def cli(ctx, symbols):
    """Warning: Undocumented Method
    """
    return ctx.gi.annotations.setSymbol(symbols)
