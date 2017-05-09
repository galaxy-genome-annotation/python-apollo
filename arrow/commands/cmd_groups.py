import click
from arrow.commands.groups.post import cli as func0
from arrow.commands.groups.updateGroup import cli as func1
from arrow.commands.groups.get import cli as func2
from arrow.commands.groups.updateOrganismPermission import cli as func3
from arrow.commands.groups.loadGroupByName import cli as func4
from arrow.commands.groups.deleteGroup import cli as func5
from arrow.commands.groups.updateMembership import cli as func6
from arrow.commands.groups.createGroup import cli as func7
from arrow.commands.groups.getOrganismPermissionsForGroup import cli as func8
from arrow.commands.groups.loadGroupById import cli as func9
from arrow.commands.groups.loadGroup import cli as func10
from arrow.commands.groups.loadGroups import cli as func11

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
cli.add_command(func11)
