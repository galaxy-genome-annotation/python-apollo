import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('updateMembership')
@click.argument("group")
@click.argument("users")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, group, users):
    """Warning: Undocumented Method
    """
    return ctx.gi.groups.updateMembership(group, users)
