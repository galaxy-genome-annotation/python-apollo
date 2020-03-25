import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, str_output


@click.command('load_gff3')
@click.argument("organism", type=str)
@click.argument("gff3", type=str)
@click.option("--test", help="Just parse the GFF3 and print results, do not push data", type=bool, default=False)
@click.option("--disable_cds_recalculation", help="Disables recalculation of CDS", type=bool, default=False)
@click.option("--use_name_for_feature", help="Uses the original name for the feature", type=bool, default=False)
@click.option(
    "--source",
    help="URL where the input dataset can be found.",
    type=str
)
@pass_context
@custom_exception
@str_output
def cli(ctx, organism, gff3, source="", test=False, disable_cds_recalculation=False, use_name_for_feature=False):
    """Load a full GFF3 into annotation track

Output:

    Loading report
    """
    return ctx.gi.annotations.load_gff3(organism, gff3, source=source, test=test,
                                        disable_cds_recalculation=disable_cds_recalculation,
                                        use_name_for_feature=use_name_for_feature)
