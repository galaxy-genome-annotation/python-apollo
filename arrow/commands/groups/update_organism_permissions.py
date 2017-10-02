import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, list_output


@click.command('update_organism_permissions')
@click.argument("group", type=str)
@click.argument("organism_name", type=str)
@click.option(
    "--administrate",
    help="Should the group have administrate privileges",
    is_flag=True
)
@click.option(
    "--write",
    help="Should the group have write privileges",
    is_flag=True
)
@click.option(
    "--read",
    help="Should the group have read privileges",
    is_flag=True
)
@click.option(
    "--export",
    help="Should the group have export privileges",
    is_flag=True
)
@pass_context
@custom_exception
@list_output
def cli(ctx, group, organism_name, administrate=False, write=False, read=False, export=False):
    """Update the group's permissions on an organism

Output:

    list of group organism permissions
    """
    return ctx.gi.groups.update_organism_permissions(group, organism_name, administrate=administrate, write=write, read=read, export=export)
