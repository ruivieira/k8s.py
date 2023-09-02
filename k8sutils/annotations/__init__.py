import functools
import subprocess
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def error(func):
    """Log a CalledProcessError as an error."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except subprocess.CalledProcessError as e:
            logging.error(e)

    return wrapper

def rethrow(func):
    """Rethrow a CalledProcessError as a normal exception."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except subprocess.CalledProcessError:
            raise  # This will re-raise the caught CalledProcessError
    return wrapper