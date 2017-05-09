import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('download')
@click.argument("uuid")

@click.option(
    "--outputFormat",
    help=""
)

@pass_context
@apollo_exception
@dict_output
def cli(ctx, uuid, outputFormat=""):
    """Warning: Undocumented Method
    """
    return ctx.gi.io.download(uuid, outputFormat=outputFormat)
