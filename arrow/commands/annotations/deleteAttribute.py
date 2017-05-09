import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('deleteAttribute')
@click.argument("feature_id")
@click.argument("key")
@click.argument("value")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, feature_id, key, value):
    """Warning: Undocumented Method
    """
    return ctx.gi.annotations.deleteAttribute(feature_id, key, value)
