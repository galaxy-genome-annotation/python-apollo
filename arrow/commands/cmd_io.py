import click
from arrow.commands.io.write import cli as func0
from arrow.commands.io.write_text import cli as func1
from arrow.commands.io.download import cli as func2
from arrow.commands.io.write_downloadable import cli as func3

@click.group()
def cli():
	pass

cli.add_command(func0)
cli.add_command(func1)
cli.add_command(func2)
cli.add_command(func3)
