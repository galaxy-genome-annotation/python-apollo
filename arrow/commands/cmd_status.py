import click
from arrow.commands.status.add_status import cli as add_status
from arrow.commands.status.delete_status import cli as delete_status
from arrow.commands.status.get_statuses import cli as get_statuses
from arrow.commands.status.show_status import cli as show_status
from arrow.commands.status.update_status import cli as update_status


@click.group()
def cli():
    pass


cli.add_command(add_status)
cli.add_command(delete_status)
cli.add_command(get_statuses)
cli.add_command(show_status)
cli.add_command(update_status)
