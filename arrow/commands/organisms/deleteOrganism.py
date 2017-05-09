import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('deleteOrganism')
@click.argument("organismId")


@pass_context
@apollo_exception
@dict_output
def cli(ctx, organismId):
    """Warning: Undocumented Method
    """
    return ctx.gi.organisms.deleteOrganism(organismId)
