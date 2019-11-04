import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, dict_output


@click.command('update_organism')
@click.argument("organism_id", type=str)
@click.argument("organism_data", type=click.File('rb+'))
@click.option(
    "--blatdb",
    help="Path to 2bit index of the genome for Blat (Blat 2bit data can also be in organism_data in directory 'searchDatabaseData')",
    type=click.File('rb+')
)
@click.option(
    "--common_name",
    help="Organism common name",
    type=str
)
@click.option(
    "--genus",
    help="Genus",
    type=str
)
@click.option(
    "--species",
    help="Species",
    type=str
)
@click.option(
    "--public",
    help="User's email",
    is_flag=True
)
@click.option(
    "--metadata",
    help="JSON formatted arbitrary metadata",
    type=str
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, organism_id, organism_data, blatdb="", common_name="", genus="", species="", public="", metadata=""):
    """Update an organism using the remote organism API.

Output:

    a dictionary with information about the updated organism
    """
    return ctx.gi.remote.update_organism(organism_id, organism_data, blatdb=blatdb, common_name=common_name, genus=genus, species=species, public=public, metadata=metadata)
