import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('setTranslationStart')
@click.argument("uniquename")
@click.argument("start")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, uniquename, start):
    """Warning: Undocumented Method
    """
    return ctx.gi.annotations.setTranslationStart(uniquename, start)
