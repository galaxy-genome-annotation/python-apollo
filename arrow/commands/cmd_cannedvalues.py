import click
from arrow.commands.cannedvalues.add_value import cli as add_value
from arrow.commands.cannedvalues.delete_value import cli as delete_value
from arrow.commands.cannedvalues.get_values import cli as get_values
from arrow.commands.cannedvalues.show_value import cli as show_value
from arrow.commands.cannedvalues.update_value import cli as update_value


@click.group()
def cli():
    pass


cli.add_command(add_value)
cli.add_command(delete_value)
cli.add_command(get_values)
cli.add_command(show_value)
cli.add_command(update_value)
