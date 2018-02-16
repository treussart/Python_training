"""
>>> foo = 2
>>> def bar():
...     foo = 3
>>> foo
2
>>> class Parent():
...     x = 1
>>> class Child1(Parent):
...     pass
>>> class Child2(Parent):
...     pass
>>> Parent.x, Child1.x, Child2.x
(1, 1, 1)
>>> Child1.x = 2
>>> Parent.x, Child1.x, Child2.x
(1, 2, 1)
>>> Parent.x = 3
>>> Parent.x, Child1.x, Child2.x
(3, 2, 3)
>>> def append_to(element, to=list()): # or []
...     to.append(element)
...     return to
>>> my_list = append_to(12)
>>> my_list
[12]
>>> my_other_list = append_to(42)
>>> my_other_list
[12, 42]
# Python’s default arguments are evaluated once when the function is
# defined, not each time the function is called (like it is in say,
# Ruby). This means that if you use a mutable default argument and
# mutate it, you will and have mutated that object for all future calls
# to the function as well.
# Solution:
>>> def append_to(element, to=None):
...     if to is None:
...         to = []
...     to.append(element)
...     return to
>>> my_list = append_to(12)
>>> my_list
[12]
>>> my_other_list = append_to(42)
>>> my_other_list
[42]
"""
