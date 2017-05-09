import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('updateOrganismInfo')
@click.argument("organismId")
@click.argument("commonName")
@click.argument("directory")

@click.option(
    "--blatdb",
    help=""
)
@click.option(
    "--species",
    help=""
)
@click.option(
    "--genus",
    help=""
)
@click.option(
    "--public",
    help=""
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, organismId, commonName, directory, blatdb="", species="", genus="", public=False):
    """Warning: Undocumented Method
    """
    return ctx.gi.organisms.updateOrganismInfo(organismId, commonName, directory, blatdb=blatdb, species=species, genus=genus, public=public)
