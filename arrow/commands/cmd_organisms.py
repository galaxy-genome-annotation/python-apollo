import click
from arrow.commands.organisms.post import cli as func0
from arrow.commands.organisms.get import cli as func1
from arrow.commands.organisms.findOrganismByCn import cli as func2
from arrow.commands.organisms.updateOrganismInfo import cli as func3
from arrow.commands.organisms.deleteOrganismFeatures import cli as func4
from arrow.commands.organisms.getSequencesForOrganism import cli as func5
from arrow.commands.organisms.addOrganism import cli as func6
from arrow.commands.organisms.deleteOrganism import cli as func7
from arrow.commands.organisms.findAllOrganisms import cli as func8
from arrow.commands.organisms.findOrganismById import cli as func9

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
