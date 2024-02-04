The exercise in `grammar.py` requires you to learn one or two new things.
The first thing to consider is that you've already learned how to iterate through lists:

```python
>>> my_list = [1, 2, 3, 4]
>>> for i in my_list:
...    print(i)
1
2
3
4
>>>
```

You've also learned that a string is a sequence of letters and numbers like `"one fish"` or `"Bruno"`.

The first thing to learn is that strings are actually lists. So the following will work:

```python
>>> my_string = "Bruno"
>>> for i in my_string:
...     print(i)
B
r
u
n
o
>>>
```

The second thing to learn is something called *concatenation*, which means joining things together. When you use the `+` operator on strings and characters, they are concatenated. For example:

```python
>>> n = "Bruno " + "Medina"
>>> print(n)
Bruno Medina
>>>
```

The third thing is that strings have functions that they can use to change them. For example, if I want to make all of the characters in a string upper case, I'd call the `upper()` method on the string. For example:

```python
>>> n = "bruno"
>>> print(n.upper())
BRUNO
>>>
```

This also works on single characters, I can get the first character this way and print it in upper case, so 
```python
>>> n = "bruno"
>>> print(n[0])
B
>>>
```

Whith this information, plus what you already know, plus a bit of problem solving, you'll be ble to finish the `grammar.py` exercise.
