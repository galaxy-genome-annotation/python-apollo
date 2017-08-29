import click
from arrow.commands.remote.add_organism import cli as func0

@click.group()
def cli():
    pass

cli.add_command(func0)
