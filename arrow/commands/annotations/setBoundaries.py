import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('setBoundaries')
@click.argument("uniquename")
@click.argument("start")
@click.argument("end")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, uniquename, start, end):
    """Warning: Undocumented Method
    """
    return ctx.gi.annotations.setBoundaries(uniquename, start, end)
