import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('delete_features')
@click.argument("organism_id", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, organism_id):
    """Remove features of an organism

Output:

    an empty dictionary
    """
    return ctx.gi.organisms.delete_features(organism_id)
