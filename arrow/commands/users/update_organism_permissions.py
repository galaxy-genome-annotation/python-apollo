import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('update_organism_permissions')
@click.argument("user", type=str)
@click.argument("organism", type=str)
@click.option(
    "--administrate",
    help="Grants administrative privileges",
    is_flag=True
)
@click.option(
    "--write",
    help="Grants write privileges",
    is_flag=True
)
@click.option(
    "--export",
    help="Grants export privileges",
    is_flag=True
)
@click.option(
    "--read",
    help="Grants read privileges",
    is_flag=True
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, user, organism, administrate=False, write=False, export=False, read=False):
    """Update the permissions of a user on a specified organism

Output:

    a dictionary containing user's organism permissions
    """
    return ctx.gi.users.update_organism_permissions(user, organism, administrate=administrate, write=write, export=export, read=read)
