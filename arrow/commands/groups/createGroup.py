import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('createGroup')
@click.argument("name")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, name):
    """Warning: Undocumented Method
    """
    return ctx.gi.groups.createGroup(name)
