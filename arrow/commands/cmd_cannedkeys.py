import click
from arrow.commands.cannedkeys.add_key import cli as add_key
from arrow.commands.cannedkeys.delete_key import cli as delete_key
from arrow.commands.cannedkeys.get_keys import cli as get_keys
from arrow.commands.cannedkeys.show_key import cli as show_key
from arrow.commands.cannedkeys.update_key import cli as update_key


@click.group()
def cli():
    pass


cli.add_command(add_key)
cli.add_command(delete_key)
cli.add_command(get_keys)
cli.add_command(show_key)
cli.add_command(update_key)
