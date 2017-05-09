import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('addAttributes')
@click.argument("feature_id")
@click.argument("attributes")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, feature_id, attributes):
    """Warning: Undocumented Method
    """
    return ctx.gi.annotations.addAttributes(feature_id, attributes)
