import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('update_attribute')
@click.argument("feature_id", type=str)
@click.argument("attribute_key", type=str)
@click.argument("old_value", type=str)
@click.argument("new_value", type=str)
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
def cli(ctx, feature_id, attribute_key, old_value, new_value, organism="", sequence=""):
    """Delete an attribute from a feature

Output:

    A standard apollo feature dictionary ({"features": [{...}]})
    """
    return ctx.gi.annotations.update_attribute(feature_id, attribute_key, old_value, new_value, organism=organism, sequence=sequence)
