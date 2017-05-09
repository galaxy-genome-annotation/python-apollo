import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('setTranslationEnd')
@click.argument("uniquename")
@click.argument("end")


@pass_context
@apollo_exception
@dict_output
def cli(ctx, uniquename, end):
    """Warning: Undocumented Method
    """
    return ctx.gi.annotations.setTranslationEnd(uniquename, end)
