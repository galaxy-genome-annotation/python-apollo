import click
from arrow.commands.cannedcomments.post import cli as func0
from arrow.commands.cannedcomments.findCommentByValue import cli as func1
from arrow.commands.cannedcomments.updateComment import cli as func2
from arrow.commands.cannedcomments.get import cli as func3
from arrow.commands.cannedcomments.addComment import cli as func4
from arrow.commands.cannedcomments.findAllComments import cli as func5
from arrow.commands.cannedcomments.deleteComment import cli as func6
from arrow.commands.cannedcomments.findCommentById import cli as func7

@click.group()
def cli():
	pass

cli.add_command(func0)
cli.add_command(func1)
cli.add_command(func2)
cli.add_command(func3)
cli.add_command(func4)
cli.add_command(func5)
cli.add_command(func6)
cli.add_command(func7)
