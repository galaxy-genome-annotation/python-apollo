from __future__ import absolute_import
from __future__ import print_function
import json
import wrapt
from .io import error
import sys
import traceback


@wrapt.decorator
def custom_exception(wrapped, instance, args, kwargs):
    try:
        return wrapped(*args, **kwargs)
    except Exception as e:
        if hasattr(e, 'body'):
            try:
                error(json.loads(e.body)['err_msg'])
            except json.decoder.JSONDecodeError:
                error(str(e))
        else:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            error(''.join(lines))
            error(str(e))
            ctx = args[0]
            ctx.exit(1)


@wrapt.decorator
def list_output(wrapped, instance, args, kwargs):
    output = wrapped(*args, **kwargs)
    print((json.dumps(output, indent=4)))


@wrapt.decorator
def dict_output(wrapped, instance, args, kwargs):
    output = wrapped(*args, **kwargs)
    print((json.dumps(output, indent=4)))


@wrapt.decorator
def str_output(wrapped, instance, args, kwargs):
    print(wrapped(*args, **kwargs))


@wrapt.decorator
def None_output(wrapped, instance, args, kwargs):
    print(wrapped(*args, **kwargs))


def _arg_split(ctx, param, value):
    # split columns by ',' and remove whitespace
    columns = [c.strip() for c in value.split(',')]
    return columns
