import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('create_group')
@click.argument("name", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, name):
    """Create a new group

Output:

    Group information dictionary
    """
    return ctx.gi.groups.create_group(name)
