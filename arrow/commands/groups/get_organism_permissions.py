import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, list_output


@click.command('get_organism_permissions')
@click.argument("group", type=str)
@pass_context
@custom_exception
@list_output
def cli(ctx, group):
    """Get the group's organism permissions

Output:

    a list containing organism permissions (if any)
    """
    return ctx.gi.groups.get_organism_permissions(group)
