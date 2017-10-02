import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('update_key')
@click.argument("id_number", type=int)
@click.argument("new_key", type=str)
@click.option(
    "--metadata",
    help="Optional metadata",
    type=str
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, id_number, new_key, metadata=""):
    """Update a canned key

Output:

    an empty dictionary
    """
    return ctx.gi.cannedkeys.update_key(id_number, new_key, metadata=metadata)
