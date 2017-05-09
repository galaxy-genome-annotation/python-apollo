import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('getComments')
@click.argument("feature_id")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, feature_id):
    """Warning: Undocumented Method
    """
    return ctx.gi.annotations.getComments(feature_id)
