import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('setStatus')
@click.argument("statuses")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, statuses):
    """Warning: Undocumented Method
    """
    return ctx.gi.annotations.setStatus(statuses)
