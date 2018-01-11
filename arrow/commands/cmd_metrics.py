import click
from arrow.commands.metrics.get_metrics import cli as func0


@click.group()
def cli():
    pass


cli.add_command(func0)
