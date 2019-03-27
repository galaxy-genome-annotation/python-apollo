import click
from arrow.commands.groups.create_group import cli as func0
from arrow.commands.groups.delete_group import cli as func1
from arrow.commands.groups.get_group_admin import cli as func2
from arrow.commands.groups.get_group_creator import cli as func3
from arrow.commands.groups.get_groups import cli as func4
from arrow.commands.groups.get_organism_permissions import cli as func5
from arrow.commands.groups.show_group import cli as func6
from arrow.commands.groups.update_group import cli as func7
from arrow.commands.groups.update_group_admin import cli as func8
from arrow.commands.groups.update_membership import cli as func9
from arrow.commands.groups.update_organism_permissions import cli as func10


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
cli.add_command(func8)
cli.add_command(func9)
cli.add_command(func10)
