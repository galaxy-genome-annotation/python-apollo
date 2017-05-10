import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('addKey')
@click.argument("key")

@click.option(
    "--metadata",
    help=""
)

@pass_context
@apollo_exception
@dict_output
def cli(ctx, key, metadata=""):
    """TODO: Undocumented

Output:

     ???
        
    """
    return ctx.gi.cannedkeys.addKey(key, metadata=metadata)
