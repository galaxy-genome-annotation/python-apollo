import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('add_key')
@click.argument("key", type=str)
@click.option(
    "--metadata",
    help="Optional metadata",
    type=str
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, key, metadata=""):
    """Add a canned key

Output:

    A dictionnary containing canned key description
    """
    return ctx.gi.cannedkeys.add_key(key, metadata=metadata)
