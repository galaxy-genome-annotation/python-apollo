import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, list_output


@click.command('get_groups')
@click.option(
    "--name",
    help="Only return group(s) with given name",
    type=str
)
@pass_context
@custom_exception
@list_output
def cli(ctx, name=""):
    """Get all the groups

Output:

    list of a dictionaries containing group information
    """
    return ctx.gi.groups.get_groups(name=name)
