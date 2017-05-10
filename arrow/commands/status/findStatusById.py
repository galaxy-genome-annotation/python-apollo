import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output, _arg_split

@click.command('findStatusById')
@click.argument("id_number")


@pass_context
@apollo_exception
@dict_output
def cli(ctx, id_number):
    """TODO: Undocumented

Output:

     ???
        
    """
    return ctx.gi.status.findStatusById(id_number)
