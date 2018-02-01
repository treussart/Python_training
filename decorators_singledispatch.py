from functools import singledispatch


x = 6


def power_lower(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).lower()
    return wrapper


def power_space(func):
    def wrapper(*args, **kwargs):
        return ' '.join(list(func(*args, **kwargs)))
    return wrapper


def power_trim(nbr):
    def power_trim_func(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)[:nbr]
        return wrapper
    return power_trim_func


@singledispatch
@power_trim(x)
@power_lower
@power_space
def test(value):
    raise NotImplementedError('Unsupported type')


@test.register(str)
@power_trim(x)
@power_lower
@power_space
def _(value):
    # Must return a string
    return value


@test.register(int)
@power_trim(x)
@power_lower
@power_space
def _(value):
    # Must return a string
    return str(value)


@test.register(list)
@power_trim(x)
@power_space
def _(value):
    # Must return a string
    return ''.join(value)


print(test("Test_Value"))
print(test(666))
print(test(['e', '3', 'Rtt']))
