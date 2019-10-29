import click
from arrow.commands.remote.add_organism import cli as add_organism
from arrow.commands.remote.add_track import cli as add_track
from arrow.commands.remote.delete_organism import cli as delete_organism
from arrow.commands.remote.delete_track import cli as delete_track
from arrow.commands.remote.update_organism import cli as update_organism
from arrow.commands.remote.update_track import cli as update_track


@click.group()
def cli():
    pass


cli.add_command(add_organism)
cli.add_command(add_track)
cli.add_command(delete_organism)
cli.add_command(delete_track)
cli.add_command(update_organism)
cli.add_command(update_track)
