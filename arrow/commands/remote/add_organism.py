import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, dict_output


@click.command('add_organism')
@click.argument("common_name", type=str)
@click.argument("organism_data", type=click.File('rb+'))
@click.option(
    "--blatdb",
    help="Path to 2bit index of the genome for Blat (Blat 2bit data can also be in organism_data in directory 'searchDatabaseData')",
    type=click.File('rb+')
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
    help="should the organism be public",
    is_flag=True
)
@click.option(
    "--non_default_translation_table",
    help="The translation table number for the organism (if different than that of the server's default)",
    type=int
)
@click.option(
    "--metadata",
    help="JSON formatted arbitrary metadata",
    type=str
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, common_name, organism_data, blatdb="", genus="", species="", public="", non_default_translation_table="", metadata=""):
    """Add an organism using the remote organism API.

Output:

    a dictionary with information about the new organism
    """
    return ctx.gi.remote.add_organism(common_name, organism_data, blatdb=blatdb, genus=genus, species=species, public=public, non_default_translation_table=non_default_translation_table, metadata=metadata)
