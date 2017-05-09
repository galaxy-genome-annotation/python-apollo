import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('addComments')
@click.argument("feature_id")
@click.argument("comments")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, feature_id, comments):
    """Warning: Undocumented Method
    """
    return ctx.gi.annotations.addComments(feature_id, comments)
