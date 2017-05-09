import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('get')
@click.argument("client_method")
@click.argument("get_params")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, client_method, get_params):
    """
    """
    return ctx.gi.status.get(client_method, get_params)
