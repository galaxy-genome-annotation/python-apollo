import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('loadGroups')

@click.option(
    "--group",
    help=""
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, group=""):
    """Warning: Undocumented Method
    """
    return ctx.gi.groups.loadGroups(group=group)
