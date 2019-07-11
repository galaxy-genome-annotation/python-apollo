import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('updateComment')
@click.argument("id_number")
@click.argument("new_value")
@click.option(
    "--metadata",
    help=""
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, id_number, new_value, metadata=""):
    """TODO: Undocumented

Output:

    ???
    """
    return ctx.gi.cannedcomments.updateComment(id_number, new_value, metadata=metadata)
