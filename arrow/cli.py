from __future__ import absolute_import
import os
import sys
import click
import json

from .io import error
from .config import read_global_config, global_config_path  # noqa, ditto
from .apollo import get_apollo_instance
from apollo import set_logging_level
from arrow import __version__  # noqa, ditto

CONTEXT_SETTINGS = dict(auto_envvar_prefix='ARROW', help_option_names=['-h', '--help'])


class Context(object):

    def __init__(self):
        self.verbose = False
        self.home = os.getcwd()
        self._global_config = None

    @property
    def global_config(self):
        if self._global_config is None:
            self._global_config = read_global_config()
        return self._global_config

    def log(self, msg, *args):
        """Logs a message to stderr."""
        if args:
            msg %= args
        click.echo(msg, file=sys.stderr)

    def vlog(self, msg, *args):
        """Logs a message to stderr only if verbose is enabled."""
        if self.verbose:
            self.log(msg, *args)

    def exit(self, exit_code):
        self.vlog("Exiting arrow with exit code [%d]" % exit_code)
        sys.exit(exit_code)


pass_context = click.make_pass_decorator(Context, ensure=True)
cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                          'commands'))


def list_cmds():
    rv = []
    for filename in os.listdir(cmd_folder):
        if filename.endswith('.py') and \
           filename.startswith('cmd_'):
            rv.append(filename[len("cmd_"):-len(".py")])
    rv.sort()
    return rv


def list_subcmds(parent):
    rv = []
    for filename in os.listdir(os.path.join(cmd_folder, parent)):
        if filename.endswith('.py') and \
           not filename.startswith('__'):
            rv.append(filename[:-len(".py")])
    rv.sort()
    return rv


def name_to_command(parent, name):
    try:
        if sys.version_info[0] == 2:
            if parent:
                parent = parent.encode('ascii', 'replace')
            name = name.encode('ascii', 'replace')

        if parent:
            mod_name = 'arrow.commands.%s.%s' % (parent, name)
        else:
            mod_name = 'arrow.commands.cmd_' + name
        mod = __import__(mod_name, None, None, ['cli'])
    except ImportError as e:
        error("Problem loading command %s, exception %s" % (name, e))
        return
    return mod.cli


class ArrowCLI(click.MultiCommand):

    def list_commands(self, ctx):
        # We pre-calculate this so it works more nicely within packaged
        # versions of arrow. Please feel free to fix this?

        commands = [
            'init',
            'annotations',
            'cannedcomments',
            'cannedkeys',
            'cannedvalues',
            'groups',
            'io',
            'metrics',
            'organisms',
            'status',
            'users'
        ]
        return commands

    def get_command(self, ctx, name):
        return name_to_command(None, name)


@click.command(cls=ArrowCLI, context_settings=CONTEXT_SETTINGS)
@click.version_option(__version__)
@click.option('-v', '--verbose', is_flag=True,
              help='Enables verbose mode.')
@click.option(
    "-a",
    "--apollo_instance",
    help='name of apollo instance from %s' % global_config_path(),
    default='__default',
    show_default=True,
    required=True
)
@click.option(
    "-l",
    "--log-level",
    help='Logging level',
    type=click.Choice(['debug', 'info', 'warn', 'error', 'critical']),
    default='warn',
    show_default=True,
)
@pass_context
def arrow(ctx, apollo_instance, verbose, log_level):
    """Command line wrappers around Apollo functions. While this sounds
    unexciting, with arrow and jq you can easily build powerful command line
    scripts."""
    set_logging_level(log_level)

    # We abuse this, knowing that calls to one will fail.
    try:
        ctx.gi = get_apollo_instance(apollo_instance)
    except TypeError:
        pass
        # ctx.log("Could not access Galaxy instance configuration")

    ctx.verbose = verbose


def json_loads(data):
    """Load json data, allowing - to represent stdin."""
    if data is None:
        return ""

    if data == "-":
        return json.load(sys.stdin)
    elif os.path.exists(data):
        with open(data, 'r') as handle:
            return json.load(handle)
    else:
        return json.loads(data)
