class Foo:
    def __init__(self, a):
        self.a = a

    def bar(self, b):
        return self.a + b


foo = Foo(1)

# Unbound methods
print(Foo.bar(foo, 2))
bar = Foo.bar
print(bar(foo, 2))

# Bound methods
print(foo.bar(2))


# MonkeyPatch
def baz(self):
    return self.a * 2

Foo.baz = baz
print(Foo.baz(foo))
print(foo.baz())

import types
foo.baz = types.MethodType(baz, foo)
print(foo.baz())