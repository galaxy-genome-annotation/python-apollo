import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, dict_output, _arg_split

@click.command('update_status')
@click.argument("old_value", type=str)
@click.argument("new_value", type=str)


@pass_context
@custom_exception
@dict_output
def cli(ctx, old_value, new_value):
    """Update a status name

Output:

     an empty dictionary
        
    """
    return ctx.gi.status.update_status(old_value, new_value)
