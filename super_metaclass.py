
class MetaPeople(type):
    def __call__(self, *args, **kwargs):
        print("Call Class {}".format(self.__name__))
        return type.__call__(self, *args, **kwargs)

    def __new__(cls, *args, **kwargs):
        print("Created Class {}".format(cls.__name__))
        # return super(MetaPeople, cls).__new__(cls, *args, **kwargs)
        return type.__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print("Initialized Class {}".format(self.__class__))
        type.__init__(self, *args, **kwargs)


class Dad(metaclass=MetaPeople):
    def __new__(cls, username):
        print("Created Class {0}, username: {1}".format(cls.__name__, username))
        # return super(Dad, cls).__new__(cls)
        return object.__new__(cls)

    def __init__(self, username):
        print("Initialized Class {}".format(self.__class__))
        self.username = username

    def __str__(self):
        return self.username


class Mum(metaclass=MetaPeople):
    def __new__(cls, username, skills):
        print("Created Class {0}, username: {1}".format(cls.__name__, username))
        return object.__new__(cls)

    def __init__(self, username, skills):
        print("Initialized Class {}".format(self.__class__))
        self.username = username
        self.skills = skills

    def __str__(self):
        return self.username + str(self.skills)


dad = Dad("daddy")
print(dad)
mum = Mum("mummy", ['play', 'humor'])
print(mum)
