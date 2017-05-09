import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('updateGroup')
@click.argument("group")
@click.argument("newName")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, group, newName):
    """Warning: Undocumented Method
    """
    return ctx.gi.groups.updateGroup(group, newName)
