import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('get')
@click.argument("client_method")
@click.argument("get_params")


@pass_context
@apollo_exception
@dict_output
def cli(ctx, client_method, get_params):
    """
    """
    return ctx.gi.cannedvalues.get(client_method, get_params)
