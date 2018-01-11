import click
from arrow.commands.cannedcomments.add_comment import cli as func0
from arrow.commands.cannedcomments.delete_comment import cli as func1
from arrow.commands.cannedcomments.get_comments import cli as func2
from arrow.commands.cannedcomments.show_comment import cli as func3
from arrow.commands.cannedcomments.update_comment import cli as func4


@click.group()
def cli():
    pass


cli.add_command(func0)
cli.add_command(func1)
cli.add_command(func2)
cli.add_command(func3)
cli.add_command(func4)
