import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('update_value')
@click.argument("id_number", type=int)
@click.argument("new_value", type=str)
@click.option(
    "--metadata",
    help="Optional metadata",
    type=str
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, id_number, new_value, metadata=""):
    """Update a canned value

Output:

    an empty dictionary
    """
    return ctx.gi.cannedvalues.update_value(id_number, new_value, metadata=metadata)
