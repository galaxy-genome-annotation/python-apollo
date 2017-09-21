import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('get_metrics')
@pass_context
@custom_exception
@dict_output
def cli(ctx):
    """Get all server metrics

Output:

    A dictionary with all of the server timing / metrics
    """
    return ctx.gi.metrics.get_metrics()
