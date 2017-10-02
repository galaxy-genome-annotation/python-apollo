import click
from arrow.commands.status.add_status import cli as func0
from arrow.commands.status.delete_status import cli as func1
from arrow.commands.status.get_statuses import cli as func2
from arrow.commands.status.show_status import cli as func3
from arrow.commands.status.update_status import cli as func4


@click.group()
def cli():
    pass


cli.add_command(func0)
cli.add_command(func1)
cli.add_command(func2)
cli.add_command(func3)
cli.add_command(func4)
