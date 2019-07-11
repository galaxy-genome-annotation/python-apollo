import click
from arrow.commands.organisms.add_organism import cli as add_organism
from arrow.commands.organisms.delete_features import cli as delete_features
from arrow.commands.organisms.delete_organism import cli as delete_organism
from arrow.commands.organisms.get_organism_creator import cli as get_organism_creator
from arrow.commands.organisms.get_organisms import cli as get_organisms
from arrow.commands.organisms.get_sequences import cli as get_sequences
from arrow.commands.organisms.show_organism import cli as show_organism
from arrow.commands.organisms.update_metadata import cli as update_metadata
from arrow.commands.organisms.update_organism import cli as update_organism


@click.group()
def cli():
    pass


cli.add_command(add_organism)
cli.add_command(delete_features)
cli.add_command(delete_organism)
cli.add_command(get_organism_creator)
cli.add_command(get_organisms)
cli.add_command(get_sequences)
cli.add_command(show_organism)
cli.add_command(update_metadata)
cli.add_command(update_organism)
