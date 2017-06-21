import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, dict_output, _arg_split

@click.command('addStatus')
@click.argument("value")


@pass_context
@custom_exception
@dict_output
def cli(ctx, value):
    """TODO: Undocumented

Output:

     ???
        
    """
    return ctx.gi.status.addStatus(value)
