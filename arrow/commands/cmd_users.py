import click
from arrow.commands.users.activate_user import cli as activate_user
from arrow.commands.users.add_to_group import cli as add_to_group
from arrow.commands.users.create_user import cli as create_user
from arrow.commands.users.delete_user import cli as delete_user
from arrow.commands.users.get_organism_permissions import cli as get_organism_permissions
from arrow.commands.users.get_user_creator import cli as get_user_creator
from arrow.commands.users.get_users import cli as get_users
from arrow.commands.users.inactivate_user import cli as inactivate_user
from arrow.commands.users.remove_from_group import cli as remove_from_group
from arrow.commands.users.show_user import cli as show_user
from arrow.commands.users.update_organism_permissions import cli as update_organism_permissions
from arrow.commands.users.update_user import cli as update_user


@click.group()
def cli():
    pass


cli.add_command(activate_user)
cli.add_command(add_to_group)
cli.add_command(create_user)
cli.add_command(delete_user)
cli.add_command(get_organism_permissions)
cli.add_command(get_user_creator)
cli.add_command(get_users)
cli.add_command(inactivate_user)
cli.add_command(remove_from_group)
cli.add_command(show_user)
cli.add_command(update_organism_permissions)
cli.add_command(update_user)
