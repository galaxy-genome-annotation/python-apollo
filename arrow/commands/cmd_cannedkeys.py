import click
from arrow.commands.cannedkeys.findKeyByValue import cli as func0
from arrow.commands.cannedkeys.findAllKeys import cli as func1
from arrow.commands.cannedkeys.findKeyById import cli as func2
from arrow.commands.cannedkeys.deleteKey import cli as func3
from arrow.commands.cannedkeys.updateKey import cli as func4
from arrow.commands.cannedkeys.addKey import cli as func5

@click.group()
def cli():
	pass

cli.add_command(func0)
cli.add_command(func1)
cli.add_command(func2)
cli.add_command(func3)
cli.add_command(func4)
cli.add_command(func5)
