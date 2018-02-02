class People:
    def __new__(cls):
        print("People Created Class {0}".format(cls.__name__))
        # return super(Dad, cls).__new__(cls)
        return object.__new__(cls)

    def __init__(self):
        print("Dad Initialized Class {}".format(self.__class__.__name__))

    def __str__(self):
        return "str: People"

    @staticmethod
    def run(value):
        print("People run " + str(value))


class Dad(People):
    def __new__(cls, username):
        print("Dad Created Class {0}, username: {1}".format(cls.__name__, username))
        # return super(Dad, cls).__new__(cls)
        return object.__new__(cls)

    def __init__(self, username):
        print("Dad Initialized Class {}".format(self.__class__.__name__))
        self.username = username

    def __str__(self):
        return self.username


class Mum(People):
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


print("More complicated")


class First:
    def __init__(self):
        print("first")


class Second(First):
    def __init__(self):
        super(First, self).__init__()
        print("second")


class Third(First):
    # Cannot inhertited of Second
    def __init__(self):
        super(First, self).__init__()
        print("third")


class Fourth(Second, Third):
    def __init__(self):
        super(Second, self).__init__()
        super(Third, self).__init__()
        print("that's it")


print(First())
print(Second())
print(Third())
print(Fourth())
