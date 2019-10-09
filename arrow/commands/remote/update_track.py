import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, dict_output


@click.command('update_track')
@click.argument("organism_id", type=str)
@click.argument("track_config", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, organism_id, track_config):
    """Update the configuration of a track that has already been added to the organism. Will not update data for the track.

Output:

    a dictionary with information about all tracks on the organism
    """
    return ctx.gi.remote.update_track(organism_id, json_loads(track_config))
