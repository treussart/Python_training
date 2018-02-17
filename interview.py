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
# output
>>> A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
>>> A0
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
>>> A1 = range(10)
>>> A1
range(0, 10)
>>> A2 = sorted([i for i in A1 if i in A0])
>>> A2
[]
>>> A3 = sorted([A0[s] for s in A0])
>>> A3
[1, 2, 3, 4, 5]
>>> A4 = [i for i in A1 if i in A3]
>>> A4
[1, 2, 3, 4, 5]
>>> A5 = {i:i*i for i in A1}
>>> A5
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> A6 = [[i,i*i] for i in A1]
>>> A6
[[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]
# other
>>> def f(x,l=[]):
...     for i in range(x):
...         l.append(i*i)
...     print(l)
...
>>> f(2)
[0, 1]
>>> f(3,[3,2,1])
[3, 2, 1, 0, 1, 4]
>>> f(3)
[0, 1, 0, 1, 4]
"""
