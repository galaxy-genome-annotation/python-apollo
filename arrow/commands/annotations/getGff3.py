import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('getGff3')
@click.argument("uniquenames")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, uniquenames):
    """Warning: Undocumented Method
    """
    return ctx.gi.annotations.getGff3(uniquenames)
