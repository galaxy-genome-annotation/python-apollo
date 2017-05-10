import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('delete_group')
@click.argument("group", type=str)


@pass_context
@apollo_exception
@dict_output
def cli(ctx, group):
    """Delete a group
    """
    return ctx.gi.groups.delete_group(group)
