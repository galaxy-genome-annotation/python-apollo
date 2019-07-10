import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, dict_output


@click.command('delete_track')
@click.argument("organism_id", type=str)
@click.argument("track_label", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, organism_id, track_label):
    """Remove a track from an organism

Output:

    a dictionary with information about the deleted track
    """
    return ctx.gi.remote.delete_track(organism_id, track_label)
