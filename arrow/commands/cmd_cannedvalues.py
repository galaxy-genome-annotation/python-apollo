import click
from arrow.commands.cannedvalues.add_value import cli as func0
from arrow.commands.cannedvalues.delete_value import cli as func1
from arrow.commands.cannedvalues.get_values import cli as func2
from arrow.commands.cannedvalues.show_value import cli as func3
from arrow.commands.cannedvalues.update_value import cli as func4


@click.group()
def cli():
    pass


cli.add_command(func0)
cli.add_command(func1)
cli.add_command(func2)
cli.add_command(func3)
cli.add_command(func4)
