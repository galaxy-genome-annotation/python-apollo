import click
from arrow.commands.io.write import cli as func0
from arrow.commands.io.download import cli as func1

@click.group()
def cli():
	pass

cli.add_command(func0)
cli.add_command(func1)
