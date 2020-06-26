import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import custom_exception, str_output


@click.command('load_gff3')
@click.argument("organism", type=str)
@click.argument("gff3", type=str)
@click.option(
    "--source",
    help="URL where the input dataset can be found.",
    type=str
)
@click.option(
    "--batch_size",
    help="Size of batches before writing",
    default="1",
    show_default=True,
    type=int
)
@click.option(
    "--test",
    help="Run in dry run mode",
    is_flag=True
)
@click.option(
    "--use_name",
    help="Use the given name instead of generating one.",
    is_flag=True
)
@click.option(
    "--disable_cds_recalculation",
    help="Disable CDS recalculation and instead use the one provided",
    is_flag=True
)
@click.option(
    "--timing",
    help="Output loading performance metrics",
    is_flag=True
)
@pass_context
@custom_exception
@str_output
def cli(ctx, organism, gff3, source="", batch_size=1, test=False, use_name=False, disable_cds_recalculation=False, timing=False):
    """Load a full GFF3 into annotation track

Output:

    Loading report
    """
    return ctx.gi.annotations.load_gff3(organism, gff3, source=source, batch_size=batch_size, test=test, use_name=use_name, disable_cds_recalculation=disable_cds_recalculation, timing=timing)
