from apollo.exceptions import APIErrorResponseException

from decorator import decorator


@decorator
def raise_error_decorator(fn):
    def wrapper(*args, **kwargs):
        r = fn(*args, **kwargs)
        if type(r) is dict and "error" in r:
            raise APIErrorResponseException("Apollo Error in function \"%s\":\n\t-%s" %
                                            (fn.__name__, r["error"]))
        return r
    return wrapper
