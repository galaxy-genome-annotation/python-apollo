import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('getOrganismPermissionsForGroup')
@click.argument("group")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, group):
    """Warning: Undocumented Method
    """
    return ctx.gi.groups.getOrganismPermissionsForGroup(group)
