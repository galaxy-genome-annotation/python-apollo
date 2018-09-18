import click
from arrow.commands.annotations.add_attribute import cli as func0
from arrow.commands.annotations.add_comment import cli as func1
from arrow.commands.annotations.add_dbxref import cli as func2
from arrow.commands.annotations.add_feature import cli as func3
from arrow.commands.annotations.add_transcript import cli as func4
from arrow.commands.annotations.delete_attribute import cli as func5
from arrow.commands.annotations.delete_dbxref import cli as func6
from arrow.commands.annotations.delete_feature import cli as func7
from arrow.commands.annotations.delete_sequence_alteration import cli as func8
from arrow.commands.annotations.duplicate_transcript import cli as func9
from arrow.commands.annotations.flip_strand import cli as func10
from arrow.commands.annotations.get_comments import cli as func11
from arrow.commands.annotations.get_feature_sequence import cli as func12
from arrow.commands.annotations.get_features import cli as func13
from arrow.commands.annotations.get_gff3 import cli as func14
from arrow.commands.annotations.get_search_tools import cli as func15
from arrow.commands.annotations.get_sequence_alterations import cli as func16
from arrow.commands.annotations.merge_exons import cli as func17
from arrow.commands.annotations.set_boundaries import cli as func18
from arrow.commands.annotations.set_description import cli as func19
from arrow.commands.annotations.set_longest_orf import cli as func20
from arrow.commands.annotations.set_name import cli as func21
from arrow.commands.annotations.set_readthrough_stop_codon import cli as func22
from arrow.commands.annotations.set_sequence import cli as func23
from arrow.commands.annotations.set_status import cli as func24
from arrow.commands.annotations.set_symbol import cli as func25
from arrow.commands.annotations.set_translation_end import cli as func26
from arrow.commands.annotations.set_translation_start import cli as func27
from arrow.commands.annotations.update_attribute import cli as func28
from arrow.commands.annotations.update_dbxref import cli as func29


@click.group()
def cli():
    pass


cli.add_command(func0)
cli.add_command(func1)
cli.add_command(func2)
cli.add_command(func3)
cli.add_command(func4)
cli.add_command(func5)
cli.add_command(func6)
cli.add_command(func7)
cli.add_command(func8)
cli.add_command(func9)
cli.add_command(func10)
cli.add_command(func11)
cli.add_command(func12)
cli.add_command(func13)
cli.add_command(func14)
cli.add_command(func15)
cli.add_command(func16)
cli.add_command(func17)
cli.add_command(func18)
cli.add_command(func19)
cli.add_command(func20)
cli.add_command(func21)
cli.add_command(func22)
cli.add_command(func23)
cli.add_command(func24)
cli.add_command(func25)
cli.add_command(func26)
cli.add_command(func27)
cli.add_command(func28)
cli.add_command(func29)
