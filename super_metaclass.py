
class MetaPeople(type):
    def __call__(cls, *args, **kwargs):
        print("MetaPeople Call Class {}".format(cls.__name__))
        return type.__call__(cls, *args, **kwargs)

    def __new__(mcs, *args, **kwargs):
        print("MetaPeople Created Class {}".format(mcs.__name__))
        # return super(MetaPeople, mcs).__new__(mcs, *args, **kwargs)
        return type.__new__(mcs, *args, **kwargs)

    def __init__(cls, *args, **kwargs):
        print("MetaPeople Initialized Class {}".format(cls.__name__))
        type.__init__(cls, *args, **kwargs)


class SubMetaPeople(MetaPeople):
    def __call__(cls, *args, **kwargs):
        print("SubMetaPeople Call Class {}".format(cls.__name__))
        return type.__call__(cls, *args, **kwargs)

    def __new__(mcs, *args, **kwargs):
        print("SubMetaPeople Created Class {}".format(mcs.__name__))
        # return super(SubMetaPeople, mcs).__new__(mcs, *args, **kwargs)
        return type.__new__(mcs, *args, **kwargs)

    def __init__(cls, *args, **kwargs):
        print("SubMetaPeople Initialized Class {}".format(cls.__name__))
        type.__init__(cls, *args, **kwargs)


class Dad(metaclass=MetaPeople):
    def __new__(cls, username):
        print("Dad Created Class {0}, username: {1}".format(cls.__name__, username))
        # return super(Dad, cls).__new__(cls)
        return object.__new__(cls)

    def __init__(self, username):
        print("Dad Initialized Class {}".format(self.__class__.__name__))
        self.username = username

    def __str__(self):
        return self.username

    @staticmethod
    def run(value):
        print("Dad run " + str(value))


class Mum(metaclass=SubMetaPeople):
    def __new__(cls, username, skills):
        print("Mum Created Class {0}, username: {1}".format(cls.__name__, username))
        return object.__new__(cls)

    def __init__(self, username, skills):
        print("Mum Initialized Class {}".format(self.__class__.__name__))
        self.username = username
        self.skills = skills

    def __str__(self):
        return self.username + str(self.skills)

    @staticmethod
    def run(value):
        print("Mum run " + str(value))


class Androgyne(Dad, Mum):
    def __new__(cls, username):
        print("Androgyne Created Class {0}, username: {1}".format(cls.__name__, username))
        return object.__new__(cls)

    def __init__(self, username):
        print("Androgyne Initialized Class {}".format(self.__class__.__name__))
        skills = list()
        Dad.__init__(self, username)
        Mum.__init__(self, username, skills)

    def __str__(self):
        return self.username + str(self.skills)


dad = Dad("daddy")
dad.run("OK")
print(dad)
mum = Mum("mummy", ['play', 'humor'])
mum.run("OK")
print(mum)
androgyne = Androgyne("andy")
print(androgyne)
# Multiple inheritance
androgyne.run("OK")
print(androgyne.__dict__)

print(type(Dad))
print(type(Mum))
