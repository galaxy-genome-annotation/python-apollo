import click
from arrow.commands.users.post import cli as func0
from arrow.commands.users.get import cli as func1
from arrow.commands.users.updateOrganismPermission import cli as func2
from arrow.commands.users.updateUser import cli as func3
from arrow.commands.users.addUserToGroup import cli as func4
from arrow.commands.users.getOrganismPermissionsForUser import cli as func5
from arrow.commands.users.createUser import cli as func6
from arrow.commands.users.loadUsers import cli as func7
from arrow.commands.users.removeUserFromGroup import cli as func8
from arrow.commands.users.loadUserById import cli as func9
from arrow.commands.users.loadUser import cli as func10
from arrow.commands.users.deleteUser import cli as func11

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
