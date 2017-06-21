import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, dict_output, _arg_split

@click.command('addComment')
@click.argument("comment")

@click.option(
    "--metadata",
    help=""
)

@pass_context
@custom_exception
@dict_output
def cli(ctx, comment, metadata=""):
    """TODO: Undocumented

Output:

     ???
        
    """
    return ctx.gi.cannedcomments.addComment(comment, metadata=metadata)
