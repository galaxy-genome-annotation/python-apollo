import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('get_config')


@pass_context
@bioblend_exception
@dict_output
def cli(ctx):
    """Get a list of attributes about the Galaxy instance. More attributes will be present if the user is an admin.
    """
    return ctx.gi.config.get_config()
