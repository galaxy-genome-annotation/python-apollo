import click
from arrow.commands.cannedvalues.findAllValues import cli as func0
from arrow.commands.cannedvalues.addValue import cli as func1
from arrow.commands.cannedvalues.updateValue import cli as func2
from arrow.commands.cannedvalues.findValueByValue import cli as func3
from arrow.commands.cannedvalues.findValueById import cli as func4
from arrow.commands.cannedvalues.deleteValue import cli as func5

@click.group()
def cli():
	pass

cli.add_command(func0)
cli.add_command(func1)
cli.add_command(func2)
cli.add_command(func3)
cli.add_command(func4)
cli.add_command(func5)
