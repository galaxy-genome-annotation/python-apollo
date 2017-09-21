import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('duplicate_transcript')
@click.argument("transcript_id", type=str)
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
def cli(ctx, transcript_id, organism="", sequence=""):
    """Duplicate a transcripte

Output:

    A standard apollo feature dictionary ({"features": [{...}]})
    """
    return ctx.gi.annotations.duplicate_transcript(transcript_id, organism=organism, sequence=sequence)
