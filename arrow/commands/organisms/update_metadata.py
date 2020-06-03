import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, dict_output


@click.command('update_metadata')
@click.argument("organism_id", type=str)
@click.argument("metadata", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, organism_id, metadata):
    """Update the metadata for an existing organism.

Output:

    An empty, useless dictionary
    """
    return ctx.gi.organisms.update_metadata(organism_id, metadata)
