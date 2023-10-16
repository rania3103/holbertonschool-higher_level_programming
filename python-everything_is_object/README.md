
# [Python - Everything is object](https://via.placeholder.com/10/00b48a?text=+)

This project is a little bit different than the usual projects. The first part is only questions about Python’s specificity like “What would be the result of…”. You should read all documentation first (as usual :)), then take the time to think and brainstorm about what you think and why. Try to do this without coding anything for a few hours.

Trying examples in the Python interpreter will give you most of the answers without having to think about it. Don’t go this route. First read, then think, then brainstorm. Only then you can test in the interpreter.

It’s important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variable types.

Note that during interviews for Python positions, you will most likely have to answer to these type of questions.

All your answers should be only one line in a file. No space before or after the answer.





## [Questions](https://via.placeholder.com/10/00b48a?text=+)

[question 1](https://via.placeholder.com/10/00b48a?text=+):

```python
What function would you use to print the type of an object?
Write the name of the function in the file, without ().
```
[question 2](https://via.placeholder.com/10/00b48a?text=+):
```python
How do you get the variable identifier
(which is the memory address in the CPython implementation)?

Write the name of the function in the file, without ().
```
[question 3](https://via.placeholder.com/10/00b48a?text=+):
```python
In the following code, do a and b point to the same object? Answer with Yes or No.
>>> a = 89
>>> b = 89
```
[question 4](https://via.placeholder.com/10/00b48a?text=+):
```python
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a
```
[question 5](https://via.placeholder.com/10/00b48a?text=+):
```python
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a + 1
```
[question 6](https://via.placeholder.com/10/00b48a?text=+):
```python
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```
[question 7](https://via.placeholder.com/10/00b48a?text=+):
```python
What do these 3 lines print?

>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```
[question 8](https://via.placeholder.com/10/00b48a?text=+):
```python
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```
[question 9](https://via.placeholder.com/10/00b48a?text=+):
```pyton
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```
[question 10](https://via.placeholder.com/10/00b48a?text=+):
```python
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```
[question 11](https://via.placeholder.com/10/00b48a?text=+):
```python
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```
[question 12](https://via.placeholder.com/10/00b48a?text=+):
```python
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```
[question 13](https://via.placeholder.com/10/00b48a?text=+):
```python
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```
[question 14](https://via.placeholder.com/10/00b48a?text=+):
```python
What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```
[question 15](https://via.placeholder.com/10/00b48a?text=+):
```python
What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```
[question 16](https://via.placeholder.com/10/00b48a?text=+):
```python
What does this script print?

def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```
[question 17](https://via.placeholder.com/10/00b48a?text=+):
```python
What does this script print?

def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```
[question 18](https://via.placeholder.com/10/00b48a?text=+):
```python
What does this script print?

def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```
[question 20](https://via.placeholder.com/10/00b48a?text=+):
```python
a = ()
Is a a tuple? Answer with Yes or No.
```
[question 21](https://via.placeholder.com/10/00b48a?text=+):
```python
a = (1, 2)
Is a a tuple? Answer with Yes or No.
```
[question 22](https://via.placeholder.com/10/00b48a?text=+):
```python
a = (1)
Is a a tuple? Answer with Yes or No.
```
[question 23](https://via.placeholder.com/10/00b48a?text=+):
```python
a = (1, )
Is a a tuple? Answer with Yes or No.
```
[question 24](https://via.placeholder.com/10/00b48a?text=+):
```python
What does this script print?

a = (1)
b = (1)
a is b
```
[question 25](https://via.placeholder.com/10/00b48a?text=+):
```python
What does this script print?

a = (1, 2)
b = (1, 2)
a is b
```
[question 26](https://via.placeholder.com/10/00b48a?text=+):
```python
What does this script print?

a = ()
b = ()
a is b
```
[question 27](https://via.placeholder.com/10/00b48a?text=+):
```python
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.
```
[question 28](https://via.placeholder.com/10/00b48a?text=+):
```python
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.
```
## [Authors](https://via.placeholder.com/10/00b48a?text=+)

- [@rania3103](https://www.github.com/rania3103)


