class Output:
    def __repr__(self):
        return 'REPR'

    def __str__(self):
        return 'STR'


print(Output())


class Sic(object):
    def __repr__(object): return 'repr'


print(str(Sic()))

print(repr(Sic()))


class Sic(object):
    def __str__(object): return 'str'


print(str(Sic()))

print(repr(Sic()))
