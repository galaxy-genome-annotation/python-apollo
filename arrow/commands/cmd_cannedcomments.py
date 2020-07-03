import click
from arrow.commands.cannedcomments.add_comment import cli as add_comment
from arrow.commands.cannedcomments.delete_comment import cli as delete_comment
from arrow.commands.cannedcomments.get_comments import cli as get_comments
from arrow.commands.cannedcomments.show_comment import cli as show_comment
from arrow.commands.cannedcomments.update_comment import cli as update_comment


@click.group()
def cli():
    pass


cli.add_command(add_comment)
cli.add_command(delete_comment)
cli.add_command(get_comments)
cli.add_command(show_comment)
cli.add_command(update_comment)
