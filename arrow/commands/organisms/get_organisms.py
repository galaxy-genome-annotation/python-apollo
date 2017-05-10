import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('get_organisms')

@click.option(
    "--common_name",
    help=""
)
@click.option(
    "--cn",
    help="Optionally filter on common name",
    type=str
)

@pass_context
@apollo_exception
@dict_output
def cli(ctx, common_name="", cn=None):
    """Get all organisms

Output:

     Organisms information
        
    """
    kwargs = {}
    if cn and len(cn) > 0:
        kwargs['cn'] = cn

    return ctx.gi.organisms.get_organisms(common_name=common_name, **kwargs)
