import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('addFeature')
@click.argument("feature")

@click.option(
    "--trustme",
    help=""
)

@pass_context
@apollo_exception
@dict_output
def cli(ctx, feature, trustme=False):
    """Warning: Undocumented Method
    """
    return ctx.gi.annotations.addFeature(feature, trustme=trustme)
