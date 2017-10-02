import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('add_status')
@click.argument("status", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, status):
    """Add a status value

Output:

    A dictionnary containing status description
    """
    return ctx.gi.status.add_status(status)
