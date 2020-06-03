import click
from arrow.commands.annotations.add_attribute import cli as add_attribute
from arrow.commands.annotations.add_comment import cli as add_comment
from arrow.commands.annotations.add_dbxref import cli as add_dbxref
from arrow.commands.annotations.add_feature import cli as add_feature
from arrow.commands.annotations.add_features import cli as add_features
from arrow.commands.annotations.add_transcript import cli as add_transcript
from arrow.commands.annotations.add_transcripts import cli as add_transcripts
from arrow.commands.annotations.delete_attribute import cli as delete_attribute
from arrow.commands.annotations.delete_dbxref import cli as delete_dbxref
from arrow.commands.annotations.delete_feature import cli as delete_feature
from arrow.commands.annotations.delete_sequence_alteration import cli as delete_sequence_alteration
from arrow.commands.annotations.duplicate_transcript import cli as duplicate_transcript
from arrow.commands.annotations.flip_strand import cli as flip_strand
from arrow.commands.annotations.get_comments import cli as get_comments
from arrow.commands.annotations.get_feature_sequence import cli as get_feature_sequence
from arrow.commands.annotations.get_features import cli as get_features
from arrow.commands.annotations.get_gff3 import cli as get_gff3
from arrow.commands.annotations.get_search_tools import cli as get_search_tools
from arrow.commands.annotations.get_sequence_alterations import cli as get_sequence_alterations
from arrow.commands.annotations.load_gff3 import cli as load_gff3
from arrow.commands.annotations.load_legacy_gff3 import cli as load_legacy_gff3
from arrow.commands.annotations.merge_exons import cli as merge_exons
from arrow.commands.annotations.set_boundaries import cli as set_boundaries
from arrow.commands.annotations.set_description import cli as set_description
from arrow.commands.annotations.set_longest_orf import cli as set_longest_orf
from arrow.commands.annotations.set_name import cli as set_name
from arrow.commands.annotations.set_readthrough_stop_codon import cli as set_readthrough_stop_codon
from arrow.commands.annotations.set_sequence import cli as set_sequence
from arrow.commands.annotations.set_status import cli as set_status
from arrow.commands.annotations.set_symbol import cli as set_symbol
from arrow.commands.annotations.set_translation_end import cli as set_translation_end
from arrow.commands.annotations.set_translation_start import cli as set_translation_start
from arrow.commands.annotations.update_attribute import cli as update_attribute
from arrow.commands.annotations.update_dbxref import cli as update_dbxref


@click.group()
def cli():
    pass


cli.add_command(add_attribute)
cli.add_command(add_comment)
cli.add_command(add_dbxref)
cli.add_command(add_feature)
cli.add_command(add_features)
cli.add_command(add_transcript)
cli.add_command(add_transcripts)
cli.add_command(delete_attribute)
cli.add_command(delete_dbxref)
cli.add_command(delete_feature)
cli.add_command(delete_sequence_alteration)
cli.add_command(duplicate_transcript)
cli.add_command(flip_strand)
cli.add_command(get_comments)
cli.add_command(get_feature_sequence)
cli.add_command(get_features)
cli.add_command(get_gff3)
cli.add_command(get_search_tools)
cli.add_command(get_sequence_alterations)
cli.add_command(load_gff3)
cli.add_command(load_legacy_gff3)
cli.add_command(merge_exons)
cli.add_command(set_boundaries)
cli.add_command(set_description)
cli.add_command(set_longest_orf)
cli.add_command(set_name)
cli.add_command(set_readthrough_stop_codon)
cli.add_command(set_sequence)
cli.add_command(set_status)
cli.add_command(set_symbol)
cli.add_command(set_translation_end)
cli.add_command(set_translation_start)
cli.add_command(update_attribute)
cli.add_command(update_dbxref)
