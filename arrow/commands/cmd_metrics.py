import click
from arrow.commands.metrics.get_metrics import cli as get_metrics


@click.group()
def cli():
    pass


cli.add_command(get_metrics)
