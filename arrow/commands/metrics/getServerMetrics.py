import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('getServerMetrics')


@pass_context
@bioblend_exception
@dict_output
def cli(ctx):
    """Get all server metrics
    """
    return ctx.gi.metrics.getServerMetrics()
