def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(args, kwargs)
        except Exception as e0:
            return f'error : {e0}'

    return wrapper


@catch_errors
def lets_do_anything(llist: list, a):
    return llist.index(a)


a = int(input())
llist = [1, 2, 3]
print(lets_do_anything(llist, a))
