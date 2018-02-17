"""
>>> def f(a:int, *, b):
...     return a, b
...
>>> f(1, b=2)
(1, 2)
>>>
>>>
>>> def clip(text:str="45", max_len:'int > 0'=80) -> dict:
...     return {"test": text}
...
>>> clip.__annotations__
{'text': <class 'str'>, 'max_len': 'int > 0', 'return': <class 'dict'>}
>>>
>>> clip(max_len=-3)
{'test': '45'}
>>>
>>>
>>> def test(arg1:str, arg2:'not important', arg3:int=0):
...     assert arg1
...     assert arg2
...     assert arg3
...
>>> test.__annotations__
{'arg1': <class 'str'>, 'arg2': 'not important', 'arg3': <class 'int'>}
"""
