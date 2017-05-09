import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('updateOrganismPermission')
@click.argument("group")
@click.argument("organismName")

@click.option(
    "--administrate",
    help=""
)
@click.option(
    "--write",
    help=""
)
@click.option(
    "--read",
    help=""
)
@click.option(
    "--export",
    help=""
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, group, organismName, administrate=False, write=False, read=False, export=False):
    """Warning: Undocumented Method
    """
    return ctx.gi.groups.updateOrganismPermission(group, organismName, administrate=administrate, write=write, read=read, export=export)
