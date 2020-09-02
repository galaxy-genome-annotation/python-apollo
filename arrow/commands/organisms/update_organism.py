import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, dict_output


@click.command('update_organism')
@click.argument("organism_id", type=str)
@click.argument("common_name", type=str)
@click.argument("directory", type=str)
@click.option(
    "--blatdb",
    help="Server-side Blat directory for the organism",
    type=str
)
@click.option(
    "--species",
    help="Species",
    type=str
)
@click.option(
    "--genus",
    help="Genus",
    type=str
)
@click.option(
    "--public",
    help="User's email",
    is_flag=True
)
@click.option(
    "--no_reload_sequences",
    help="Set this if you don't want Apollo to reload genome sequences (no change in genome sequence)",
    is_flag=True
)
@click.option(
    "--suppress_output",
    help="Suppress output of all organisms (true / false) (default false)",
    is_flag=True
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, organism_id, common_name, directory, blatdb="", species="", genus="", public=False, no_reload_sequences=False, suppress_output=False):
    """Update an organism

Output:

    a dictionary with information about the updated organism
    """
    return ctx.gi.organisms.update_organism(organism_id, common_name, directory, blatdb=blatdb, species=species, genus=genus, public=public, no_reload_sequences=no_reload_sequences, suppress_output=suppress_output)
