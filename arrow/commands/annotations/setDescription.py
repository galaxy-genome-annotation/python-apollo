import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('setDescription')
@click.argument("featureDescriptions")


@pass_context
@apollo_exception
@dict_output
def cli(ctx, featureDescriptions):
    """Warning: Undocumented Method
    """
    return ctx.gi.annotations.setDescription(featureDescriptions)
