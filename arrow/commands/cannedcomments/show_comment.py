import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('show_comment')
@click.argument("value", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, value):
    """Get a specific canned comment

Output:

    A dictionnary containing canned comment description
    """
    return ctx.gi.cannedcomments.show_comment(value)
