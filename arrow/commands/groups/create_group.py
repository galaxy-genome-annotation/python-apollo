import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output, list_output, str_output

@click.command('create_group')
@click.argument("name")


@pass_context
@apollo_exception
@dict_output
def cli(ctx, name):
    """Create a new group
    """
    return ctx.gi.groups.create_group(name)
