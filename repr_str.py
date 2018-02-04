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


class Sic(object):
    def __init__(self, x=0, y=0, prout="test"):
        self.x = x
        self.y = y
        self.prout = prout

    def __repr__(self):
        keys = sorted(self.__dict__)
        items = ("{}={!r}".format(k, self.__dict__[k]) for k in keys)
        return "{}({})".format(type(self).__name__, ", ".join(items))

    def run_instance(self):
        pass

    @classmethod
    def run_class(cls):
        pass

    @staticmethod
    def run_static():
        pass


print(str(Sic(5, 7)))
