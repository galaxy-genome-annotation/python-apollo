import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('show_status')
@click.argument("status", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, status):
    """Get a specific status

Output:

    A dictionnary containing status description
    """
    return ctx.gi.status.show_status(status)
