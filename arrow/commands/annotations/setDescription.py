import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('setDescription')
@click.argument("featureDescriptions")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, featureDescriptions):
    """Warning: Undocumented Method
    """
    return ctx.gi.annotations.setDescription(featureDescriptions)
