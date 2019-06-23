def i_am_creater_dec(exp1, exp2):
    def i_am_decorator(func):
        def wrapper(args1, args2):
            try:
                return func(args1, args2)
            except exp1 as e0:
                return f'errorType = {e0}'
            except exp2 as e0:
                return f'errorType = {e0}'

        return wrapper

    return i_am_decorator


exp1 = ZeroDivisionError
exp2 = TypeError


@i_am_creater_dec(exp1, exp2)
def take_some_vars(a, b):
    return b[a]


print(take_some_vars(5, [1, 2, 3]))
