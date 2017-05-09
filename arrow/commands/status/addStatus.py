import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('addStatus')
@click.argument("value")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, value):
    """Warning: Undocumented Method
    """
    return ctx.gi.status.addStatus(value)
