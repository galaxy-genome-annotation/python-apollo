import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('updateValue')
@click.argument("id_number")
@click.argument("new_value")

@click.option(
    "--metadata",
    help=""
)

@pass_context
@apollo_exception
@dict_output
def cli(ctx, id_number, new_value, metadata=""):
    """Warning: Undocumented Method
    """
    return ctx.gi.cannedvalues.updateValue(id_number, new_value, metadata=metadata)
