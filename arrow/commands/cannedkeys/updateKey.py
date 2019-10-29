import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('updateKey')
@click.argument("id_number")
@click.argument("new_key")
@click.option(
    "--metadata",
    help=""
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, id_number, new_key, metadata=""):
    """TODO: Undocumented

Output:

    ???
    """
    return ctx.gi.cannedkeys.updateKey(id_number, new_key, metadata=metadata)
