import click
from arrow.commands.cannedkeys.add_key import cli as func0
from arrow.commands.cannedkeys.delete_key import cli as func1
from arrow.commands.cannedkeys.get_keys import cli as func2
from arrow.commands.cannedkeys.show_key import cli as func3
from arrow.commands.cannedkeys.update_key import cli as func4


@click.group()
def cli():
    pass


cli.add_command(func0)
cli.add_command(func1)
cli.add_command(func2)
cli.add_command(func3)
cli.add_command(func4)
