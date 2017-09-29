import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, dict_output, _arg_split

@click.command('delete_status')
@click.argument("status", type=str)


@pass_context
@custom_exception
@dict_output
def cli(ctx, status):
    """Delete a status

Output:

     an empty dictionary
        
    """
    return ctx.gi.status.delete_status(status)
