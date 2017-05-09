import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('mergeExons')
@click.argument("exonA")
@click.argument("exonB")


@pass_context
@apollo_exception
@dict_output
def cli(ctx, exonA, exonB):
    """Warning: Undocumented Method
    """
    return ctx.gi.annotations.mergeExons(exonA, exonB)
