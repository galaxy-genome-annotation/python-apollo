import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('findAllValues')
@pass_context
@custom_exception
@dict_output
def cli(ctx):
    """TODO: Undocumented

Output:

    ???
    """
    return ctx.gi.cannedvalues.findAllValues()
