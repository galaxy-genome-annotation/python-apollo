import click
from arrow.cli import pass_context
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
@pass_context
@custom_exception
@dict_output
def cli(ctx, organism_id, common_name, directory, blatdb="", species="", genus="", public=False):
    """Update an organism

Output:

    a dictionary with information about the new organism
    """
    return ctx.gi.organisms.update_organism(organism_id, common_name, directory, blatdb=blatdb, species=species, genus=genus, public=public)
