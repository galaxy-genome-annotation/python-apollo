import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, dict_output


@click.command('add_transcripts')
@click.option(
    "--transcripts",
    help="Transcript data",
    type=str,
    multiple=True
)
@click.option(
    "--suppress_history",
    help="Suppress the history of this operation",
    is_flag=True
)
@click.option(
    "--suppress_events",
    help="Suppress instant update of the user interface",
    is_flag=True
)
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
def cli(ctx, transcripts=None, suppress_history=False, suppress_events=False, organism="", sequence=""):
    """Add a list of transcript annotations

Output:

    A standard apollo feature dictionary ({"features": [{...}]})
    """
    return ctx.gi.annotations.add_transcripts(transcripts=transcripts, suppress_history=suppress_history, suppress_events=suppress_events, organism=organism, sequence=sequence)
