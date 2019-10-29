import click
from arrow.commands.groups.create_group import cli as create_group
from arrow.commands.groups.delete_group import cli as delete_group
from arrow.commands.groups.get_group_admin import cli as get_group_admin
from arrow.commands.groups.get_group_creator import cli as get_group_creator
from arrow.commands.groups.get_groups import cli as get_groups
from arrow.commands.groups.get_organism_permissions import cli as get_organism_permissions
from arrow.commands.groups.show_group import cli as show_group
from arrow.commands.groups.update_group import cli as update_group
from arrow.commands.groups.update_group_admin import cli as update_group_admin
from arrow.commands.groups.update_membership import cli as update_membership
from arrow.commands.groups.update_organism_permissions import cli as update_organism_permissions


@click.group()
def cli():
    pass


cli.add_command(create_group)
cli.add_command(delete_group)
cli.add_command(get_group_admin)
cli.add_command(get_group_creator)
cli.add_command(get_groups)
cli.add_command(get_organism_permissions)
cli.add_command(show_group)
cli.add_command(update_group)
cli.add_command(update_group_admin)
cli.add_command(update_membership)
cli.add_command(update_organism_permissions)
