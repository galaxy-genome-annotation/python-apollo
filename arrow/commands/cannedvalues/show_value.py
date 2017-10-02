import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('show_value')
@click.argument("value", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, value):
    """Get a specific canned value

Output:

    A dictionnary containing canned value description
    """
    return ctx.gi.cannedvalues.show_value(value)
