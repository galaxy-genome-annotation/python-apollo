import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('get_search_tools')
@pass_context
@custom_exception
@dict_output
def cli(ctx):
    """Get the search tools available

Output:

    dictionary containing the search tools and their metadata.
          For example::

            {
                "sequence_search_tools": {
                    "blat_prot": {
                        "name": "Blat protein",
                        "search_class": "org.bbop.apollo.sequence.search.blat.BlatCommandLineProteinToNucleotide",
                        "params": "",
                        "search_exe": "/usr/local/bin/blat"
                    },
                    "blat_nuc": {
                        "name": "Blat nucleotide",
                        "search_class": "org.bbop.apollo.sequence.search.blat.BlatCommandLineNucleotideToNucleotide",
                        "params": "",
                        "search_exe": "/usr/local/bin/blat"
                    }
                }
            }
    """
    return ctx.gi.annotations.get_search_tools()
