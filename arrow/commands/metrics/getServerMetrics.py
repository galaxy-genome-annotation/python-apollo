import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('getServerMetrics')


@pass_context
@apollo_exception
@dict_output
def cli(ctx):
    """Get all server metrics
    """
    return ctx.gi.metrics.getServerMetrics()
