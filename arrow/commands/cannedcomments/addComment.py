import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('addComment')
@click.argument("comment")

@click.option(
    "--metadata",
    help=""
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, comment, metadata=""):
    """Warning: Undocumented Method
    """
    return ctx.gi.cannedcomments.addComment(comment, metadata=metadata)
