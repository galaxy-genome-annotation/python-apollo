import click
from arrow.commands.cannedvalues.addValue import cli as addValue
from arrow.commands.cannedvalues.add_value import cli as add_value
from arrow.commands.cannedvalues.deleteValue import cli as deleteValue
from arrow.commands.cannedvalues.delete_value import cli as delete_value
from arrow.commands.cannedvalues.findAllValues import cli as findAllValues
from arrow.commands.cannedvalues.findValueById import cli as findValueById
from arrow.commands.cannedvalues.findValueByValue import cli as findValueByValue
from arrow.commands.cannedvalues.get_values import cli as get_values
from arrow.commands.cannedvalues.show_value import cli as show_value
from arrow.commands.cannedvalues.updateValue import cli as updateValue
from arrow.commands.cannedvalues.update_value import cli as update_value


@click.group()
def cli():
    pass


cli.add_command(addValue)
cli.add_command(add_value)
cli.add_command(deleteValue)
cli.add_command(delete_value)
cli.add_command(findAllValues)
cli.add_command(findValueById)
cli.add_command(findValueByValue)
cli.add_command(get_values)
cli.add_command(show_value)
cli.add_command(updateValue)
cli.add_command(update_value)
