import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('download')
@click.argument("uuid", type=str)

@click.option(
    "--output_format",
    help="Output format of the data, either \"gzip\" or \"text\"",
    type=str
)

@pass_context
@apollo_exception
@dict_output
def cli(ctx, uuid, output_format="gzip"):
    """Download pre-prepared data by UUID
    """
    return ctx.gi.io.download(uuid, output_format=output_format)
