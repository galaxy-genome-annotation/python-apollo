import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('getSequencesForOrganism')
@click.argument("commonName")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, commonName):
    """Warning: Undocumented Method
    """
    return ctx.gi.organisms.getSequencesForOrganism(commonName)
