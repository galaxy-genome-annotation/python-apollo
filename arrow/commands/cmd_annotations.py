import click
from arrow.commands.annotations.getGff3 import cli as func0
from arrow.commands.annotations.post import cli as func1
from arrow.commands.annotations.setDescription import cli as func2
from arrow.commands.annotations.addFeature import cli as func3
from arrow.commands.annotations.getSequenceAlterations import cli as func4
from arrow.commands.annotations.setTranslationStart import cli as func5
from arrow.commands.annotations.setReadthroughStopCodon import cli as func6
from arrow.commands.annotations.get import cli as func7
from arrow.commands.annotations.deleteSequenceAlteration import cli as func8
from arrow.commands.annotations.deleteAttribute import cli as func9
from arrow.commands.annotations.mergeExons import cli as func10
from arrow.commands.annotations.getSequenceSearchTools import cli as func11
from arrow.commands.annotations.setLongestOrf import cli as func12
from arrow.commands.annotations.setStatus import cli as func13
from arrow.commands.annotations.setSequence import cli as func14
from arrow.commands.annotations.addAttributes import cli as func15
from arrow.commands.annotations.duplicateTranscript import cli as func16
from arrow.commands.annotations.setName import cli as func17
from arrow.commands.annotations.addTranscript import cli as func18
from arrow.commands.annotations.setTranslationEnd import cli as func19
from arrow.commands.annotations.flipStrand import cli as func20
from arrow.commands.annotations.setNames import cli as func21
from arrow.commands.annotations.getFeatures import cli as func22
from arrow.commands.annotations.getCannedComments import cli as func23
from arrow.commands.annotations.setSymbol import cli as func24
from arrow.commands.annotations.getSequence import cli as func25
from arrow.commands.annotations.deleteFeatures import cli as func26
from arrow.commands.annotations.getComments import cli as func27
from arrow.commands.annotations.setBoundaries import cli as func28
from arrow.commands.annotations.searchSequence import cli as func29
from arrow.commands.annotations.addComments import cli as func30

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
cli.add_command(func30)
