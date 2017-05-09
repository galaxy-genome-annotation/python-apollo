import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('loadGroupById')
@click.argument("groupId")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, groupId):
    """Warning: Undocumented Method
    """
    return ctx.gi.groups.loadGroupById(groupId)
