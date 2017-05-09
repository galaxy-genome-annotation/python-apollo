import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('addTranscript')
@click.argument("transcript")

@click.option(
    "--trustme",
    help=""
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, transcript, trustme=False):
    """Warning: Undocumented Method
    """
    return ctx.gi.annotations.addTranscript(transcript, trustme=trustme)
