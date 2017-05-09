import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('download')
@click.argument("uuid")

@click.option(
    "--outputFormat",
    help=""
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, uuid, outputFormat=""):
    """Warning: Undocumented Method
    """
    return ctx.gi.io.download(uuid, outputFormat=outputFormat)
