import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('download')
@click.argument("uuid", type=str)

@click.option(
    "--output_format",
    help="Output format of the data, either \"gzip\" or \"text\"",
    default="gzip",
    type=str
)

@pass_context
@apollo_exception
@dict_output
def cli(ctx, uuid, output_format="gzip"):
    """[CURRENTLY BROKEN] Download pre-prepared data by UUID

Output:

     a dictionary
        
    """
    return ctx.gi.io.download(uuid, output_format=output_format)
