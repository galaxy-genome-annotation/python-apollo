import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('deleteStatus')
@click.argument("id_number")


@pass_context
@apollo_exception
@dict_output
def cli(ctx, id_number):
    """TODO: Undocumented

Output:

     ???
        
    """
    return ctx.gi.status.deleteStatus(id_number)
