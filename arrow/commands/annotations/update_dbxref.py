import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('update_dbxref')
@click.argument("feature_id", type=str)
@click.argument("old_db", type=str)
@click.argument("old_accession", type=str)
@click.argument("new_db", type=str)
@click.argument("new_accession", type=str)
@click.option(
    "--organism",
    help="Organism Common Name",
    type=str
)
@click.option(
    "--sequence",
    help="Sequence Name",
    type=str
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, feature_id, old_db, old_accession, new_db, new_accession, organism="", sequence=""):
    """Delete a dbxref from a feature

Output:

    A standard apollo feature dictionary ({"features": [{...}]})
    """
    return ctx.gi.annotations.update_dbxref(feature_id, old_db, old_accession, new_db, new_accession, organism=organism, sequence=sequence)
