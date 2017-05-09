import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('addKey')
@click.argument("key")

@click.option(
    "--metadata",
    help=""
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, key, metadata=""):
    """Warning: Undocumented Method
    """
    return ctx.gi.cannedkeys.addKey(key, metadata=metadata)
