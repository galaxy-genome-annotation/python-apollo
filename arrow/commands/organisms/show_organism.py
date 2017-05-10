import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('show_organism')
@click.argument("organism_id", type=str)


@pass_context
@apollo_exception
@dict_output
def cli(ctx, organism_id):
    """Get information about a specific organism. Due to the lack of an API, this call requires fetching the entire list of organisms and iterating through. If you find this painfully slow, please submit a bug report upstream.

Output:

     a dictionary containing the organism's information
        
    """
    return ctx.gi.organisms.show_organism(organism_id)
