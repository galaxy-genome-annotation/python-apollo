import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('download')
@click.argument("uuid", type=str)
@click.option(
    "--output_format",
    help="Output format of the data, either \"gzip\" or \"text\"",
    default="gzip",
    show_default=True,
    type=str
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, uuid, output_format="gzip"):
    """[CURRENTLY BROKEN] Download pre-prepared data by UUID

Output:

    a dictionary
    """
    return ctx.gi.io.download(uuid, output_format=output_format)
