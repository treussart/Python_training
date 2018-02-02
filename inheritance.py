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
        super(People, self).__init__()
        self.username = username

    def __str__(self):
        return self.username


class Mum(People):
    def __new__(cls, username, skills):
        print("Mum Created Class {0}, username: {1}".format(cls.__name__, username))
        return object.__new__(cls)

    def __init__(self, username, skills):
        print("Mum Initialized Class {}".format(self.__class__.__name__))
        super(People, self).__init__()
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
print()
mum = Mum("mummy", ['play', 'humor'])
mum.run("OK")
print(mum)
print()
androgyne = Androgyne("andy")
print(androgyne)
# Multiple inheritance
androgyne.run("OK")
print(androgyne.__dict__)
print()
print(type(Dad))
print(type(Mum))
print()


class First:
    def __init__(self):
        print("first")


class Second(First):
    def __init__(self):
        super(First, self).__init__()
        print("second")


class Third(First):
    # Cannot inhertited of Second (because of Fourth)
    def __init__(self):
        super(First, self).__init__()
        print("third")


class Fourth(Third, Second):
    def __init__(self):
        super(Second, self).__init__()
        super(Third, self).__init__()
        print("fourth")


class Extra(Fourth): # Same as: class Extra(Fourth, Third, Second, First)
    def __init__(self):
        super(Fourth, self).__init__()
        print("extra")


print(First())
print(First.__mro__)
print(Second())
print(Second.__mro__)
print(Third())
print(Third.__mro__)
print(Fourth())
print(Fourth.__mro__)
print(Extra())
print(Extra.__mro__)
