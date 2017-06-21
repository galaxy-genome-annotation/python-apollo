import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output, _arg_split

@click.command('delete_features')
@click.argument("organism_id", type=str)


@pass_context
@apollo_exception
@dict_output
def cli(ctx, organism_id):
    """Remove features of an organism

Output:

     an empty dictionary
        
    """
    return ctx.gi.organisms.delete_features(organism_id)