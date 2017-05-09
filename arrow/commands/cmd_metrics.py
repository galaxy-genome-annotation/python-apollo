import click
from arrow.commands.metrics.post import cli as func0
from arrow.commands.metrics.getServerMetrics import cli as func1
from arrow.commands.metrics.get import cli as func2

@click.group()
def cli():
	pass

cli.add_command(func0)
cli.add_command(func1)
cli.add_command(func2)
