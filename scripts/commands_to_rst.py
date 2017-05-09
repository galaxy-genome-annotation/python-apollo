#!/usr/bin/env python

import os
import sys
from string import Template

from click.testing import CliRunner

project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_dir)

from parsec.cli import list_cmds, list_subcmds
from parsec import cli

parsec_cli = cli.parsec
runner = CliRunner()

COMMAND_TEMPLATE = Template('''
``${subcommand}`` command
${module_underline}

This section is auto-generated from the help text for the parsec command
``${command}``.

${command_help}
''')

COMMANDS_TEMPLATE = """========
Commands
========

parsec is a set of wrappers for BioBlend's API. It builds a set of small,
useful utilities for talking to Galaxy servers. Each utility is implemented as
a subcommand of ``parsec``. This section of the documentation
describes these commands.

.. toctree::
   :maxdepth: 0
"""

command_doc_dir = os.path.join("docs", "commands")
commands = COMMANDS_TEMPLATE

for command in list_cmds():
    if command == 'init':
        # Skip documenting init because it's special
        continue

    commands += "\n   commands/%s.rst" % command
    parent_doc_handle = open(os.path.join(command_doc_dir, command + ".rst"), "w")
    parent_doc_handle.write('%s\n' % command)
    parent_doc_handle.write('%s\n' % ('=' * len(command)))
    for subcommand in list_subcmds(command):

        command_obj = cli.name_to_command(command, subcommand)

        function = command_obj.callback
        raw_rst = function.__doc__

        def clean_rst_line(line):
            if line.startswith("    "):
                return line[4:]
            else:
                return line
        clean_rst = "\n".join(map(clean_rst_line, raw_rst.split("\n")))

        result = runner.invoke(parsec_cli, [command, subcommand, "--help"])
        output = result.output
        lines = output.split("\n")
        new_lines = []
        help_lines = False
        option_lines = False

        for line in lines:
            if line.startswith("Usage: "):
                new_lines.append("**Usage**::\n\n    %s" % line[len("Usage: "):])
                new_lines.append("\n**Help**\n")
                new_lines.append(clean_rst)
                help_lines = True
            elif line.startswith("Options:"):
                help_lines = False
                new_lines.append("**Options**::\n\n")
                option_lines = True
            elif option_lines:
                new_lines.append("    %s" % line)
        text = COMMAND_TEMPLATE.safe_substitute(
            command=command,
            subcommand=subcommand,
            command_help="\n".join(new_lines),
            module_underline = "-" * (len(subcommand) + len('```` command'))
        )
        parent_doc_handle.write(text)

open(os.path.join("docs", "commands.rst"), "w").write(commands)
