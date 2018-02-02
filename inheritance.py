class People:
    def __new__(cls, **kwargs):
        print("People Created Class {0}".format(cls.__name__))
        return super(People, cls).__new__(cls)

    def __init__(self, **kwargs):
        print("Dad Initialized Class {}".format(self.__class__.__name__))

    def __str__(self):
        return "str: People"

    @staticmethod
    def run(value):
        print("People run " + str(value))


class Dad(People):
    def __new__(cls, **kwargs):
        print("Dad Created Class {0}, username: {1}".format(cls.__name__, kwargs.get('username')))
        return super(Dad, cls).__new__(cls)

    def __init__(self, **kwargs):
        print("Dad Initialized Class {}".format(self.__class__.__name__))
        super(Dad, self).__init__()
        self.username = kwargs.get('username')

    def __str__(self):
        return self.username


class Mum(People):
    def __new__(cls, **kwargs):
        print("Mum Created Class {0}, username: {1}".format(cls.__name__, kwargs.get('username')))
        return super(Mum, cls).__new__(cls)

    def __init__(self, **kwargs):
        print("Mum Initialized Class {}".format(self.__class__.__name__))
        super(Mum, self).__init__()
        self.username = kwargs.get('username')
        self.skills = kwargs.get('skills')

    def __str__(self):
        return self.username + str(self.skills)

    @staticmethod
    def run(value):
        print("Mum run " + str(value))


class Androgyne(Dad, Mum):
    def __init__(self, **kwargs):
        print("Androgyne Initialized Class {}".format(self.__class__.__name__))
        #self.skills = list()
        # super().__init__(**kwargs)
        super(Androgyne, self).__init__(**kwargs)
        #Dad.__init__(self, username)
        #Mum.__init__(self, username, self.skills)

    def __str__(self):
        return self.username + str(self.skills)


dad = Dad(username="daddy")
dad.run("OK")
print(dad)
print()
mum = Mum(username="mummy", skills=['play', 'humor'])
mum.run("OK")
print(mum)
print()
androgyne = Androgyne(username="andy", skills=list())
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
        super(Second, self).__init__()
        print("second")


class Third(First):
    # Cannot inhertited of Second (because of Fourth)
    def __init__(self):
        super(Third, self).__init__()
        print("third")


class Fourth(Third, Second):
    def __init__(self):
        super(Fourth, self).__init__()
        print("fourth")


class Extra(Fourth): # Same as: class Extra(Fourth, Third, Second, First)
    def __init__(self):
        super(Extra, self).__init__()
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
print()


class First1(object):
    def __init__(self, called_by=''):
        print("first prologue, called_by: %s" % called_by)
        super().__init__()
        print("first epilogue, called_by: %s" % called_by)


class Second2(First1):
    def __init__(self, called_by=''):
        print("second prologue, called_by: %s" % called_by)
        super(Second2, self).__init__(called_by='Second'+called_by)
        print("second epilogue, called_by: %s" % called_by)


class Third3(First1):
    def __init__(self, called_by=''):
        print("third prologue, called_by: %s" % called_by)
        super(Third3, self).__init__(called_by='Third'+called_by)
        print("third epilogue, called_by: %s" % called_by)


class Fourth4(Second2, Third3):
    def __init__(self):
        super(Fourth4, self).__init__(called_by='Fourth')
        print("that's it")


# called_by='Third' + called_by
Fourth4()
