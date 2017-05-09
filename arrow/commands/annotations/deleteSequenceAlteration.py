import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('deleteSequenceAlteration')
@click.argument("uniquename")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, uniquename):
    """Warning: Undocumented Method
    """
    return ctx.gi.annotations.deleteSequenceAlteration(uniquename)
