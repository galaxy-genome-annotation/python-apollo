import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('findValueByValue')
@click.argument("value")


@pass_context
@apollo_exception
@dict_output
def cli(ctx, value):
    """TODO: Undocumented

Output:

     ???
        
    """
    return ctx.gi.cannedvalues.findValueByValue(value)
