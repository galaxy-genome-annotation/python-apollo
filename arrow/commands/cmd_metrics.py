import click
from arrow.commands.metrics.getServerMetrics import cli as func0

@click.group()
def cli():
	pass

cli.add_command(func0)
