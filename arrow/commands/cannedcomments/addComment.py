import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('addComment')
@click.argument("comment")

@click.option(
    "--metadata",
    help=""
)

@pass_context
@apollo_exception
@dict_output
def cli(ctx, comment, metadata=""):
    """TODO: Undocumented

Output:

     ???
        
    """
    return ctx.gi.cannedcomments.addComment(comment, metadata=metadata)
