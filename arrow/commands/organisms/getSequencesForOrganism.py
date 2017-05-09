import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('getSequencesForOrganism')
@click.argument("commonName")


@pass_context
@apollo_exception
@dict_output
def cli(ctx, commonName):
    """Warning: Undocumented Method
    """
    return ctx.gi.organisms.getSequencesForOrganism(commonName)
