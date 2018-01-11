import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('show_key')
@click.argument("value", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, value):
    """Get a specific canned key

Output:

    A dictionnary containing canned key description
    """
    return ctx.gi.cannedkeys.show_key(value)
