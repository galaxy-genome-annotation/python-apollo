import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('setNames')
@click.argument("features")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, features):
    """Warning: Undocumented Method
    """
    return ctx.gi.annotations.setNames(features)
