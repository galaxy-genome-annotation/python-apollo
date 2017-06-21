import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, dict_output, _arg_split

@click.command('create_group')
@click.argument("name")


@pass_context
@custom_exception
@dict_output
def cli(ctx, name):
    """Create a new group

Output:

     Group information dictionary
        
    """
    return ctx.gi.groups.create_group(name)
