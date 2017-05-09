import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('findOrganismByCn')
@click.argument("cn")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, cn):
    """Warning: Undocumented Method
    """
    return ctx.gi.organisms.findOrganismByCn(cn)
