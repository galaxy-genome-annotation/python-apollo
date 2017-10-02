import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, list_output


@click.command('get_sequences')
@click.argument("organism_id", type=str)
@pass_context
@custom_exception
@list_output
def cli(ctx, organism_id):
    """Get the sequences for an organism

Output:

    The set of sequences associated with an organism
    """
    return ctx.gi.organisms.get_sequences(organism_id)
