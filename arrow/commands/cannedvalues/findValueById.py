import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, dict_output, _arg_split

@click.command('findValueById')
@click.argument("id_number")


@pass_context
@custom_exception
@dict_output
def cli(ctx, id_number):
    """TODO: Undocumented

Output:

     ???
        
    """
    return ctx.gi.cannedvalues.findValueById(id_number)
