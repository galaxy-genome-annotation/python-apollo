import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('get_groups')


@pass_context
@apollo_exception
@dict_output
def cli(ctx):
    """Get all the groups
    """
    return ctx.gi.groups.get_groups()
