import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, list_output


@click.command('get_organisms')
@click.option(
    "--common_name",
    help="Optionally filter on common name",
    type=str
)
@pass_context
@custom_exception
@list_output
def cli(ctx, common_name=""):
    """Get all organisms

Output:

    Organism information
    """
    return ctx.gi.organisms.get_organisms(common_name=common_name)
