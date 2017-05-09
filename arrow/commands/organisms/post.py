import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('post')
@click.argument("client_method")
@click.argument("data")

@click.option(
    "--post_params",
    help=""
)
@click.option(
    "--is_json",
    help=""
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, client_method, data, post_params="", is_json=True):
    """
    """
    return ctx.gi.organisms.post(client_method, data, post_params=post_params, is_json=is_json)
