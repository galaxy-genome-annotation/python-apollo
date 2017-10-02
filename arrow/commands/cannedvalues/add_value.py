import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('add_value')
@click.argument("value", type=str)
@click.option(
    "--metadata",
    help="Optional metadata",
    type=str
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, value, metadata=""):
    """Add a canned value

Output:

    A dictionnary containing canned value description
    """
    return ctx.gi.cannedvalues.add_value(value, metadata=metadata)
