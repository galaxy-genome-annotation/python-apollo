import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('add_organism')
@click.argument("common_name", type=str)
@click.argument("directory", type=str)
@click.option(
    "--blatdb",
    help="Server-side Blat directory for the organism",
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
@pass_context
@custom_exception
@dict_output
def cli(ctx, common_name, directory, blatdb="", genus="", species="", public=False):
    """Add an organism

Output:

    a dictionary with information about the new organism
    """
    return ctx.gi.organisms.add_organism(common_name, directory, blatdb=blatdb, genus=genus, species=species, public=public)
