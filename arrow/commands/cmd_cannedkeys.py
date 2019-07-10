import click
from arrow.commands.cannedkeys.addKey import cli as addKey
from arrow.commands.cannedkeys.add_key import cli as add_key
from arrow.commands.cannedkeys.deleteKey import cli as deleteKey
from arrow.commands.cannedkeys.delete_key import cli as delete_key
from arrow.commands.cannedkeys.findAllKeys import cli as findAllKeys
from arrow.commands.cannedkeys.findKeyById import cli as findKeyById
from arrow.commands.cannedkeys.findKeyByValue import cli as findKeyByValue
from arrow.commands.cannedkeys.get_keys import cli as get_keys
from arrow.commands.cannedkeys.show_key import cli as show_key
from arrow.commands.cannedkeys.updateKey import cli as updateKey
from arrow.commands.cannedkeys.update_key import cli as update_key


@click.group()
def cli():
    pass


cli.add_command(addKey)
cli.add_command(add_key)
cli.add_command(deleteKey)
cli.add_command(delete_key)
cli.add_command(findAllKeys)
cli.add_command(findKeyById)
cli.add_command(findKeyByValue)
cli.add_command(get_keys)
cli.add_command(show_key)
cli.add_command(updateKey)
cli.add_command(update_key)
