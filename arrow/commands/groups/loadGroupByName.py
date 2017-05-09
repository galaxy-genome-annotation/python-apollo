import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('loadGroupByName')
@click.argument("name")


@pass_context
@apollo_exception
@dict_output
def cli(ctx, name):
    """Warning: Undocumented Method
    """
    return ctx.gi.groups.loadGroupByName(name)
