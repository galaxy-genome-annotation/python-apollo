import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('delete_attribute')
@click.argument("feature_id", type=str)
@click.argument("attribute_key", type=str)
@click.argument("attribute_value", type=str)
@click.option(
    "--organism",
    help="Organism Common Name",
    type=str
)
@click.option(
    "--sequence",
    help="Sequence Name",
    type=str
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, feature_id, attribute_key, attribute_value, organism="", sequence=""):
    """Delete an attribute from a feature

Output:

    A standard apollo feature dictionary ({"features": [{...}]})
    """
    return ctx.gi.annotations.delete_attribute(feature_id, attribute_key, attribute_value, organism=organism, sequence=sequence)
