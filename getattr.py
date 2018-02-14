class Test:
    a = 20

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattr__(self, item):
        print("__getattr__ " + str(item))

    def __setattr__(self, key, value):
        print('__setattr__ key: ' + str(key) + ' value: ' + str(value))
        super(Test, self).__setattr__(key, value)

    def __getattribute__(self, item):
        print('__getattribute__ ' + str(item))
        super(Test, self).__getattribute__(item)


test = Test(0, 1)
test.x
test.y
test.x = 5
test.y = 6

test.a
test.a = 30

test.c
