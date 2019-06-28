import contextlib
from datetime import datetime


def fib(n):
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)


@contextlib.contextmanager
def time_to_do(description):
    t = datetime.now()
    try:
        yield
    finally:
        print(description, 'was doing', datetime.now() - t)


with time_to_do('Fibonacci nums'):
    fib(36)
