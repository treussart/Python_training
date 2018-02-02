from functools import singledispatch, wraps, partial


def power_lower(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).lower()
    return wrapper


def power_space(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return ' '.join(list(func(*args, **kwargs)))
    return wrapper


def power_trim(nbr):
    def power_trim_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)[:nbr]
        return wrapper
    return power_trim_func


def power_prefix(func=None, *, prefix=''):
    if func is None:
        return partial(power_prefix, prefix=prefix)
    @wraps(func)
    def wrapper(*args, **kwargs):
        return prefix + func(*args, **kwargs)
    return wrapper


@singledispatch
@power_trim(6)
@power_lower
@power_space
def test(value):
    raise NotImplementedError('Unsupported type')


@test.register(str)
@power_trim(3)
@power_lower
@power_space
def _(value):
    return value


@test.register(int)
@power_trim(8)
@power_lower
@power_space
def _(value):
    return str(value)


@test.register(list)
@power_trim(10)
@power_space
@power_prefix(prefix="***")
def _(value):
    return ''.join(value)


print(test("Test_Value"))
print(test(666))
print(test(['e', '3', 'Rtt']))
# print(test(4.8))

# wrap
print(test.__name__)
# without :
# return : wrapper
