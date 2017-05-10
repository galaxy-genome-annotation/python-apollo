import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('create_group')
@click.argument("name")


@pass_context
@apollo_exception
@dict_output
def cli(ctx, name):
    """Create a new group

Output:

     Group information dictionary
        
    """
    return ctx.gi.groups.create_group(name)
