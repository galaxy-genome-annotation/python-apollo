import click
from arrow.commands.organisms.add_organism import cli as func0
from arrow.commands.organisms.delete_features import cli as func1
from arrow.commands.organisms.delete_organism import cli as func2
from arrow.commands.organisms.get_organism_creator import cli as func3
from arrow.commands.organisms.get_organisms import cli as func4
from arrow.commands.organisms.get_sequences import cli as func5
from arrow.commands.organisms.show_organism import cli as func6
from arrow.commands.organisms.update_organism import cli as func7


@click.group()
def cli():
    pass


cli.add_command(func0)
cli.add_command(func1)
cli.add_command(func2)
cli.add_command(func3)
cli.add_command(func4)
cli.add_command(func5)
cli.add_command(func6)
cli.add_command(func7)
