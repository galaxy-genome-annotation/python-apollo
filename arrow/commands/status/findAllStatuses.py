import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('findAllStatuses')


@pass_context
@apollo_exception
@dict_output
def cli(ctx):
    """TODO: Undocumented

Output:

     ???
        
    """
    return ctx.gi.status.findAllStatuses()
