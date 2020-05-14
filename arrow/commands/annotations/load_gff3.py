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
    "--test",
    is_flag=True,
    help="Run as a test without writing.",
)
@click.option(
    "--batch_size",
    help="Number of annotations to write at a time",
    type=int
)
@click.option(
    "--use_name",
    is_flag=True,
    help="Use the given name instead of generating one.",
)
@click.option(
    "--disable_cds_recalculation",
    is_flag=True,
    help="Disable recalculation of the CDS and instead use the one provided",
)
@click.option(
    "--verbose",
    is_flag=True,
    help="Provide verbose output",
)
@pass_context
@custom_exception
@str_output
def cli(ctx, organism, gff3, source="", test=False, use_name=False, disable_cds_recalculation=False, verbose=False,
        batch_size=1):
    """Load a full GFF3 into annotation track

Output:

    Loading report
    """
    return ctx.gi.annotations.load_gff3(
        organism, gff3, source=source, test=test,
        use_name=use_name,
        disable_cds_recalculation=disable_cds_recalculation,
        verbose=verbose,
        batch_size=batch_size
    )
