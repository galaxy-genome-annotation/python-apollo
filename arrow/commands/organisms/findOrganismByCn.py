import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('findOrganismByCn')
@click.argument("cn")


@pass_context
@apollo_exception
@dict_output
def cli(ctx, cn):
    """Warning: Undocumented Method
    """
    return ctx.gi.organisms.findOrganismByCn(cn)
