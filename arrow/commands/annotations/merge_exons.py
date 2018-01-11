import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('merge_exons')
@click.argument("exon_a", type=str)
@click.argument("exon_b", type=str)
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
def cli(ctx, exon_a, exon_b, organism="", sequence=""):
    """Merge two exons

Output:

    A standard apollo feature dictionary ({"features": [{...}]})
    """
    return ctx.gi.annotations.merge_exons(exon_a, exon_b, organism=organism, sequence=sequence)
