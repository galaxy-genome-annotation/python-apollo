#!/usr/bin/env python
import importlib
import inspect
import os
import copy
import re
import glob
import argparse
import logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


import apollo as bg
IGNORE_LIST = [
    'get', 'post'
]



PARAM_TRANSLATION = {
    'str': [
        'type=str',
    ],
    'dict': [
        #TODO
        'type=str',
    ],
    'int': [
        'type=int'
    ],
    'float': [
        'type=float',
    ],
    'bool': [
        'is_flag=True',
    ],
    'list': [
        'type=str', # TODO
        'multiple=True',
    ],
    'list of str': [
        'type=str', # TODO
        'multiple=True',
    ],
    'file': [
        'type=click.File(\'rb+\')'
    ],
    'None': [],
}

class ScriptBuilder(object):

    def __init__(self):
        self.path = os.path.realpath(__file__)
        templates = glob.glob(os.path.join(os.path.dirname(self.path), 'templates', '*'))
        self.templates = {}
        for template in templates:
            (tpl_id, ext) = os.path.splitext(os.path.basename(template))
            self.templates[tpl_id] = open(template, 'r').read()

        # TODO: refactor
        self.obj = bg.ApolloInstance("http://localhost:8080", "jane@example.com", "asdf")

    def template(self, template, opts):
        return self.templates[template] % opts

    @classmethod
    def __click_option(cls, name='arg', helpstr='TODO', ptype=None, default=None):
        args = [
            '"--%s"' % name,
            'help="%s"' % (helpstr.replace('"', '\\"') if helpstr else ""),
        ]
        if default:
            args.append('default="%s"' % default)
        if ptype is not None:
            args.extend(ptype)
        return '@click.option(\n%s\n)\n' % (',\n'.join(['    ' + x for x in args]))

    @classmethod
    def __click_argument(cls, name='arg', ptype=None):
        args = [
            '"%s"' % name,
        ]
        if ptype is not None:
            args.extend(ptype)
        return '@click.argument(%s)\n' % (', '.join(args), )

    @classmethod
    def load_module(cls, module_path):
        name = '.'.join(module_path)
        return importlib.import_module(name)

    def boring(self, method_name):
        if method_name.startswith('_'):
            return True
        if 'max_retries' in method_name or 'retry_delay' in method_name or 'get_retries' in method_name:
            return True
        # TODO replace with check for height in hierachy
        return False

    def is_galaxyinstance(self, obj):
        return str(type(obj)) == "<class 'apollo.ApolloInstance'>"

    def is_function(self, obj):
        return str(type(obj)) == "<type 'instancemethod'>"

    def is_class(self, obj):
        return str(type(obj)).startswith('<class ')

    def recursive_attr_get(self, obj, section):
        if len(section) == 0:
            return obj
        elif len(section) == 1:
            try:
                return getattr(obj, section[0])
            except AttributeError:
                pass
        else:
            return getattr(self.recursive_attr_get(obj, section[0:-1]), section[-1])

    @classmethod
    def important_doc(cls, docstring):
        good = []
        if docstring is not None and len(docstring) > 0:
            for line in docstring.split('\n')[1:]:
                if line.strip() == '':
                    return ' '.join(good)
                else:
                    good.append(line.strip())
            return ' '.join(good)
        else:
            return "Warning: Undocumented Method"

    def flatten(self, x):
        # http://stackoverflow.com/a/577971
        result = []
        for el in x:
            if isinstance(el, list):
                if len(el) > 0:
                    if isinstance(el[0], str):
                        result.append(el)
                    else:
                        result.extend(self.flatten(el))
            else:
                result.append(el)
        return result

    @classmethod
    def parameter_translation(cls, k):
        try:
            return PARAM_TRANSLATION[k]
        except:
            raise Exception("Unknown parameter type " + k)

    def pair_arguments(self, func):
        try:
            argspec = inspect.getargspec(func)
        except TypeError as te:
            log.debug(te)
            return []
        # Reverse, because args are paired from the end, removing self/cls
        args = argspec.args[::-1][0:-1]

        # If nothing there after removing 'self'
        if len(args) == 0:
            return []
        if argspec.defaults is None:
            defaults = []
        else:
            defaults = list(argspec.defaults[::-1])
        # Convert all ``None`` to ""
        defaults = ["" if x is None else x for x in defaults]
        for i in range(len(args) - len(defaults)):
            defaults.append(None)
        return zip(args[::-1], defaults[::-1])

    def process(self):
        for module in dir(self.obj):
            if module[0] == '_' or module[0].upper() == module[0]:
                continue
            if module in ('client', 'apollo_url', 'username', 'password'):
                continue

            sm = getattr(bg, module)
            submodules = dir(sm)
            # Find the "...Client"
            wanted = [x for x in submodules if 'Client' in x and x != 'Client'][0]
            self.process_client(module, sm, wanted)

    def process_client(self, module, sm, ssm_name):
        log.info("Processing apollo.%s.%s", module, ssm_name)
        ssm = getattr(sm, ssm_name)
        for f in dir(ssm):
            if f[0] == '_' or f[0].upper() == f[0]:
                continue
            if f in IGNORE_LIST or '%s.%s' % (ssm, f) in IGNORE_LIST:
                continue
            self.orig(module, sm, ssm, f)
        # Write module __init__
        with open(os.path.join('arrow', 'commands', module, '__init__.py'), 'w') as handle:
            pass

        with open(os.path.join('arrow', 'commands', 'cmd_%s.py' % module), 'w') as handle:
            handle.write('import click\n')
            # for function:
            files = list(glob.glob("arrow/commands/%s/*.py" % module))
            files = [f for f in files if "__init__.py" not in f]
            for idx, path in enumerate(files):
                fn = path.replace('/', '.')[0:-3]
                handle.write('from %s import cli as func%s\n' % (fn, idx))

            handle.write('\n@click.group()\n')
            handle.write('def cli():\n')
            handle.write('\tpass\n\n')
            for i in range(len(files)):
                handle.write('cli.add_command(func%d)\n' % i)

    def orig(self, module_name, submodule, subsubmodule, function_name):
        target = [module_name, function_name]
        log.debug("Building %s", '.'.join(target))

        func = getattr(subsubmodule, function_name)
        candidate = '.'.join(target)

        argdoc = func.__doc__

        data = {
            'command_name': function_name,
            'click_arguments': "",
            'click_options': "",
            'args_with_defaults': "ctx",
            'wrapped_method_args': "",
        }
        param_docs = {}
        if argdoc is not None:
            sections = [x for x in argdoc.split("\n\n")]
            sections = [re.sub('\s+', ' ', x.strip()) for x in sections if x != '']
            paramre = re.compile(":type (?P<param_name>[^:]+): (?P<param_type>[^:]+) :param (?P<param_name2>[^:]+): (?P<desc>.+)")
            returnre = re.compile(":rtype: (?P<param_type>[^:]+) :return: (?P<desc>.+)")
            for subsec in sections:
                m = paramre.match(subsec)
                if m:
                    assert m.group('param_name') == m.group('param_name2')
                    param_docs[m.group('param_name')] = {'type': m.group('param_type'),
                                                            'desc': m.group('desc')}
                m = returnre.match(subsec)
                if m:
                    param_docs['__return__'] = {
                        'type': m.group('param_type'),
                        'desc': m.group('desc'),
                    }

        argspec = list(self.pair_arguments(func))
        data['kwarg_updates'] = ''
        data['empty_kwargs'] = ''
        # Ignore with only cls/self
        if len(argspec) > 0:
            method_signature = ['ctx']
            # Args and kwargs are separate, as args should come before kwargs
            method_signature_args = []
            method_signature_kwargs = []
            method_exec_args = []
            method_exec_kwargs = []

            def process_arg(k, v, param_type, real_type):
                log.debug("Processing %s=%s %s %s", k, v, param_type, real_type)
                orig_v = copy.deepcopy(v)
                # If v is not None, then it's a kwargs, otherwise an arg
                if v is not None:
                    # Strings must be treated specially by removing their value
                    if v == '__None__':
                        v = 'None'
                        orig_v = None
                    elif isinstance(v, str):
                        v = '"%s"' % v

                    if v == []:
                        v = None
                        orig_v = None
                    # All other instances of V are fine, e.g. boolean=False or int=1000

                    # Register twice as the method invocation uses v=k
                    if v != 'None':
                        method_signature_kwargs.append("%s=%s" % (k, v))
                        if real_type == 'dict':
                            v = 'json_loads(%s)' % v
                        method_exec_kwargs.append('%s=%s' % (k, k))
                    else:
                        # Add to signature, but NOT exec because we take care of that elsewhere.
                        method_signature_kwargs.append("%s=%s" % (k, v))

                    # TODO: refactor
                    try:
                        descstr = param_docs[k]['desc']
                    except KeyError:
                        print("Error finding %s in %s" % (k, candidate))
                        descstr = None
                    data['click_options'] += self.__click_option(name=k, helpstr=descstr, ptype=param_type, default=orig_v)
                else:
                    # Args, not kwargs
                    tk = k
                    method_signature_args.append(tk)
                    if real_type == 'dict':
                        tk = 'json_loads(%s)' % k
                    method_exec_args.append(tk)
                    data['click_arguments'] += self.__click_argument(name=k, ptype=param_type)


            argspec_keys = [x[0] for x in argspec]
            for k, v in argspec:
                if k == '__return__':
                    continue
                try:
                    param_type = self.parameter_translation(param_docs[k]['type'])
                    real_type = param_docs[k]['type']
                except Exception:
                    param_type = []
                    real_type = None
                process_arg(k, v, param_type, real_type)

            had_weird_kwargs = False
            for k in sorted(param_docs.keys()):
                if k == '__return__':
                    continue
                # Ignore things we've seen before
                if k in argspec_keys:
                    continue
                param_type = param_docs[k]['type']
                if param_type == 'list':
                    default_value = []
                else:
                    default_value = '__None__'

                process_arg(k, default_value, self.parameter_translation(param_type), param_type)
                # Booleans are diff
                if param_type == 'bool':
                    data['kwarg_updates'] += "    if %s is not None:\n        kwargs['%s'] = %s\n" % (k, k, k)
                elif param_type == 'str':
                    data['kwarg_updates'] += "    if %s and len(%s) > 0:\n        kwargs['%s'] = %s\n" % (k, k, k, k)
                had_weird_kwargs = True

            # Complete args
            data['args_with_defaults'] = ', '.join(method_signature +
                                                method_signature_args +
                                                method_signature_kwargs)
            data['wrapped_method_args'] = ', '.join(method_exec_args +
                                                    method_exec_kwargs)
            if had_weird_kwargs:
                data['wrapped_method_args'] += ', **kwargs'
                data['empty_kwargs'] = '\n    kwargs = {}\n'

        # TODO: rtype -> dict_output / list_output / text_output
        # __return__ must be in param_docs or it's a documentation BUG.
        if '__return__' not in param_docs:
            raise Exception("%s is not documented with a return type" % candidate)
        data['output_format'] = param_docs['__return__']['type']
        # We allow "list of dicts" and other such silliness.
        if ' ' in data['output_format']:
            data['output_format'] = data['output_format'][0:data['output_format'].index(' ')]

        # My function is more effective until can figure out docstring
        data['short_docstring'] = self.important_doc(argdoc)
        # Full method call
        data['wrapped_method'] = 'ctx.gi.' + candidate

        # Generate a command name, prefix everything with auto_ to identify the
        # automatically generated stuff
        cmd_name = '%s.py' % function_name
        cmd_path = os.path.join('arrow', 'commands', module_name, cmd_name)

        # Save file
        with open(cmd_path, 'w') as handle:
            handle.write(self.template('click', data))

if __name__ == '__main__':
    z = ScriptBuilder()
    parser = argparse.ArgumentParser(description='process bioblend into CLI tools')
    z.process()
