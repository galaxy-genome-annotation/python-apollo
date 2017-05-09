import click
from arrow.commands.users.post import cli as func0
from arrow.commands.users.get_users import cli as func1
from arrow.commands.users.get import cli as func2
from arrow.commands.users.updateOrganismPermission import cli as func3
from arrow.commands.users.delete_user import cli as func4
from arrow.commands.users.updateUser import cli as func5
from arrow.commands.users.update_organism_permissions import cli as func6
from arrow.commands.users.remove_from_group import cli as func7
from arrow.commands.users.update_user import cli as func8
from arrow.commands.users.addUserToGroup import cli as func9
from arrow.commands.users.getOrganismPermissionsForUser import cli as func10
from arrow.commands.users.createUser import cli as func11
from arrow.commands.users.loadUsers import cli as func12
from arrow.commands.users.show_user import cli as func13
from arrow.commands.users.get_organism_permissions import cli as func14
from arrow.commands.users.removeUserFromGroup import cli as func15
from arrow.commands.users.add_to_group import cli as func16
from arrow.commands.users.create_user import cli as func17
from arrow.commands.users.loadUserById import cli as func18
from arrow.commands.users.loadUser import cli as func19
from arrow.commands.users.deleteUser import cli as func20

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
cli.add_command(func12)
cli.add_command(func13)
cli.add_command(func14)
cli.add_command(func15)
cli.add_command(func16)
cli.add_command(func17)
cli.add_command(func18)
cli.add_command(func19)
cli.add_command(func20)
