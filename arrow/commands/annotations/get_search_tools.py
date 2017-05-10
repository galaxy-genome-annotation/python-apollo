import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output, list_output, str_output

@click.command('get_search_tools')


@pass_context
@apollo_exception
@dict_output
def cli(ctx):
    """Get the search tools available
    """
    return ctx.gi.annotations.get_search_tools()
