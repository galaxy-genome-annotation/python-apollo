import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('updateComment')
@click.argument("id_number")
@click.argument("new_value")

@click.option(
    "--metadata",
    help=""
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, id_number, new_value, metadata=""):
    """Warning: Undocumented Method
    """
    return ctx.gi.cannedcomments.updateComment(id_number, new_value, metadata=metadata)
