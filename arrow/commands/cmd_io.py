import click
from arrow.commands.io.download import cli as download
from arrow.commands.io.write_downloadable import cli as write_downloadable
from arrow.commands.io.write_text import cli as write_text


@click.group()
def cli():
    pass


cli.add_command(download)
cli.add_command(write_downloadable)
cli.add_command(write_text)
