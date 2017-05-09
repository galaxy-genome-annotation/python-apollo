import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('searchSequence')
@click.argument("searchTool")
@click.argument("sequence")
@click.argument("database")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, searchTool, sequence, database):
    """Warning: Undocumented Method
    """
    return ctx.gi.annotations.searchSequence(searchTool, sequence, database)
