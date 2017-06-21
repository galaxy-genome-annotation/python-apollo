import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, dict_output, _arg_split

@click.command('addValue')
@click.argument("value")

@click.option(
    "--metadata",
    help=""
)

@pass_context
@custom_exception
@dict_output
def cli(ctx, value, metadata=""):
    """TODO: Undocumented

Output:

     ???
        
    """
    return ctx.gi.cannedvalues.addValue(value, metadata=metadata)
