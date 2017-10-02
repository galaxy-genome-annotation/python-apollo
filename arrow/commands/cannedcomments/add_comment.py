import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('add_comment')
@click.argument("comment", type=str)
@click.option(
    "--metadata",
    help="Optional metadata",
    type=str
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, comment, metadata=""):
    """Add a canned comment

Output:

    A dictionnary containing canned comment description
    """
    return ctx.gi.cannedcomments.add_comment(comment, metadata=metadata)
