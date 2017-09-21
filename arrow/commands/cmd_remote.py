import click
from arrow.commands.remote.add_organism import cli as func0
from arrow.commands.remote.add_track import cli as func1
from arrow.commands.remote.add_track_file import cli as func2
from arrow.commands.remote.delete_organism import cli as func3
from arrow.commands.remote.delete_track import cli as func4
from arrow.commands.remote.update_track import cli as func5

@click.group()
def cli():
    pass

cli.add_command(func0)
cli.add_command(func1)
cli.add_command(func2)
cli.add_command(func3)
cli.add_command(func4)
cli.add_command(func5)
