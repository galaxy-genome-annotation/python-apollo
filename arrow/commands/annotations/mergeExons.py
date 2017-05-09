import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('mergeExons')
@click.argument("exonA")
@click.argument("exonB")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, exonA, exonB):
    """Warning: Undocumented Method
    """
    return ctx.gi.annotations.mergeExons(exonA, exonB)
