import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output, list_output, str_output

@click.command('add_feature')

@click.option(
    "--feature",
    help="Feature information",
    type=str
)
@click.option(
    "--organism",
    help="Organism Common Name",
    type=str
)
@click.option(
    "--sequence",
    help="Sequence Name",
    type=str
)

@pass_context
@apollo_exception
@dict_output
def cli(ctx, feature={}, organism="", sequence=""):
    """Add a feature
    """
    return ctx.gi.annotations.add_feature(feature=feature, organism=organism, sequence=sequence)
