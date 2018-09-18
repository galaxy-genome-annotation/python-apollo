import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('delete_dbxref')
@click.argument("feature_id", type=str)
@click.argument("db", type=str)
@click.argument("accession", type=str)
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
def cli(ctx, feature_id, db, accession, organism="", sequence=""):
    """Delete a dbxref from a feature

Output:

    A standard apollo feature dictionary ({"features": [{...}]})
    """
    return ctx.gi.annotations.delete_dbxref(feature_id, db, accession, organism=organism, sequence=sequence)
