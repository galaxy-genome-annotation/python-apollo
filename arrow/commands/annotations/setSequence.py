import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('setSequence')
@click.argument("sequence")
@click.argument("organism")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, sequence, organism):
    """Warning: Undocumented Method
    """
    return ctx.gi.annotations.setSequence(sequence, organism)
