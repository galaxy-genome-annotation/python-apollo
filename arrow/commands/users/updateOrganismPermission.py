import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('updateOrganismPermission')
@click.argument("user")
@click.argument("organism")

@click.option(
    "--administrate",
    help=""
)
@click.option(
    "--write",
    help=""
)
@click.option(
    "--export",
    help=""
)
@click.option(
    "--read",
    help=""
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, user, organism, administrate=False, write=False, export=False, read=False):
    """Warning: Undocumented Method
    """
    return ctx.gi.users.updateOrganismPermission(user, organism, administrate=administrate, write=write, export=export, read=read)
