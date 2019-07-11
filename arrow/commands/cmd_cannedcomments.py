import click
from arrow.commands.cannedcomments.addComment import cli as addComment
from arrow.commands.cannedcomments.add_comment import cli as add_comment
from arrow.commands.cannedcomments.deleteComment import cli as deleteComment
from arrow.commands.cannedcomments.delete_comment import cli as delete_comment
from arrow.commands.cannedcomments.findAllComments import cli as findAllComments
from arrow.commands.cannedcomments.findCommentById import cli as findCommentById
from arrow.commands.cannedcomments.findCommentByValue import cli as findCommentByValue
from arrow.commands.cannedcomments.get_comments import cli as get_comments
from arrow.commands.cannedcomments.show_comment import cli as show_comment
from arrow.commands.cannedcomments.updateComment import cli as updateComment
from arrow.commands.cannedcomments.update_comment import cli as update_comment


@click.group()
def cli():
    pass


cli.add_command(addComment)
cli.add_command(add_comment)
cli.add_command(deleteComment)
cli.add_command(delete_comment)
cli.add_command(findAllComments)
cli.add_command(findCommentById)
cli.add_command(findCommentByValue)
cli.add_command(get_comments)
cli.add_command(show_comment)
cli.add_command(updateComment)
cli.add_command(update_comment)
