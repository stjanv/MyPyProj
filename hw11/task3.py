from datetime import datetime


class TimEToDo(object):
    def __enter__(self):
        self.start = datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(datetime.now() - self.start)


n = 35


def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


with TimEToDo() as e:
    print(fib(n))
