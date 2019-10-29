import click
from arrow.commands.status.addStatus import cli as addStatus
from arrow.commands.status.add_status import cli as add_status
from arrow.commands.status.deleteStatus import cli as deleteStatus
from arrow.commands.status.delete_status import cli as delete_status
from arrow.commands.status.findAllStatuses import cli as findAllStatuses
from arrow.commands.status.findStatusById import cli as findStatusById
from arrow.commands.status.findStatusByValue import cli as findStatusByValue
from arrow.commands.status.get_statuses import cli as get_statuses
from arrow.commands.status.show_status import cli as show_status
from arrow.commands.status.updateStatus import cli as updateStatus
from arrow.commands.status.update_status import cli as update_status


@click.group()
def cli():
    pass


cli.add_command(addStatus)
cli.add_command(add_status)
cli.add_command(deleteStatus)
cli.add_command(delete_status)
cli.add_command(findAllStatuses)
cli.add_command(findStatusById)
cli.add_command(findStatusByValue)
cli.add_command(get_statuses)
cli.add_command(show_status)
cli.add_command(updateStatus)
cli.add_command(update_status)
