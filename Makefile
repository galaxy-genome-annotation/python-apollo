rebuild:
	python scripts/autobuilder.py
	# Docs
	rm -f docs/apollo.*.rst
	rm -f docs/commands/*
	python scripts/commands_to_rst.py
