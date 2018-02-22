import reprlib


class test:
    def __init__(self, test, test2):
        self._test = test
        self.test2 = test2

    def __repr__(self):
        repr_instance = reprlib.Repr()
        repr_instance.maxstring = 120
        keys = sorted(self.__dict__)
        items = ("{}={!r}".format(k, self.__dict__[k]) for k in keys)
        return repr_instance.repr("{}({})".format(type(self).__name__, ", ".join(items)))


a = test("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "bbbbb")
print(a)

a = test('-'* 150, 'a' * 20)
print(a)
a = test('-'* 28, 'a' * 20)
print(a)