# Python Overview

## Data Types

### Numbers

- Numbers in Python have two main forms
  - Integers - whole numbers
  - Floating Point Numbers - have a decimal

### Strings are immutables

- Indexing

```
mystring = 'abcdefg'
print(mystring[3]) # d
```

- Slicing -> beginning, starting, ending points

```
pring(mystring[4:]) # efg
print(mystring[2:5]) # cde
print(mystring[::]) # will print everything. means from beginning to end
pring(mystring[::1]) # means all the way from the beginning to the end by 1
pring(mystring[::2]) # means all the way from the beginning to the end by 2: aceg

```

- methods:

  - mystring.upper() # to uppercase
  - mystring.lower() # to lowercase
  - mystring.capitalize() # first letter uppercase
  - mystring.split() # will give us an array splitting on spaces
  - mystring.split('e') # will split after e but not include e

- Print Formatting

```
x = "Item One: {y} Item Two: {x}".format(x="dog", y="cat")
print(x) # Item One: cat Item Two: dog
```

### Lists are mutable

```
mylist = [1,2,3]
anotherlist = ['stringItem', 1,2,3,23.2,True, 'asdf', [1,2,3]]
print(len(mylist))
print(len(anotherlist))
print(mylist[-1]) # will print the last item in list
print(mylist[:3]) # just like slicing it means print from beginning till index 3 but not 3
```

- methods:

  - .append(item) will add items to the end of list
  - .extend(newlist) will combine the two lists
  - .pop() will remove the last item of the list
  - .pop(0) will remove the first index of list
  - .reverse() will reverse the order of the list
  - .sort() will sort from small to big

- accessing nested lists

```
mylist = [1,2,['x','y','z']]
print(mylist[2][1]) # it will print y
```

### List Comprehension

ex.

```
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0][0]) # will print 1

first_col = [row[0] for row in matrix]
print(first_col) # will print [1,4,7]
```

### Dictionaries are Python's version of Hash Tables (Objects in Javascript)

- They allow us to create a 'mapping' with key-value pairs
- They don't retain any order

```
my_dict = {"key1":"value", "key2": "value2","key3":{"123":[1,2,"grabme"]} }
print(my_stuff["key3"]['123'][2].upper()) # will print GRABME

my_meals = {"lunch":"pizza", "bkfast": "eggs"}
my_meals["lunch"] = "burger" # will reassign value of lunch to burger
my_meals["dinner"] = "pasta" # will add anothr key value pair to dictionary
```

### Tuples, Sets, and Booleans

- Booleans:
  - True or False
- Tuples can hold mixed data types but are immutables. Can't be changed. They use same methods as lists

```
t = (1,2,3, True, 123)
```

- Sets are unordered collections of unique elements

```
x = set()
x.add(1)
x.add(2)
x.add(4)
print(x) # {1,2,4}

converted = set([1,1,1,1,2,2,2,3,3,3,3])
print(converted) # {1,2,3}
```

### Logical Operators

- AND

```
(1 > 2) and (2 < 3)
```

- OR

```
(1 > 2) or (2 < 3)
(1 == 2) or (2 == 3) or (4 == 4)
```

- IF ELSE

```
if 1 < 2:
  print("yes")

if 1 > 2:
  print("hello")
elif 3 == 3:
  print("elif ran")
else:
  print("last")
```

### Loops

ex. list

```
seq = [1,2,3,4,5,6]

for item in seq:
  print(item)
```

ex. dictionary

```
d = {"Sam": 1, "Frank": 2, "Dan": 3}
for item in d:
  print(item) # will print the keys
  print(d[item]) # will print the value
```

ex. unpacking tuples

```
mypairs = [(1,2),(3,4),(5,6)]

for(tup1, tup2) in mypairs:
  print(tup1) # will print all the numbers 1,3,5
  print(tup2) # will print all the numbers 2,4,6
```

ex. while loops

```
i = 1
while i<5:
  print("i is: {}".format(i))
  i = i +1
```

ex. range -> Range is a generator to not store data in computer but generates the numbers to iterate. Will have only one number in memory at a time

```
l = [1,2,3,4,5]
print(range(5)) # range(0,5)
print(list(range(0,5))) # [0,1,2,3,4]
print(list(range(0,20,2))) # [0,2,4,6,8,10,12,14,16,18]

for item in range(10):
  print(item) # 1,2,3,4,5,6,7,8,9
```

ex. list comprehension loop

```
x = [1,2,3,4]
out = []
for num in x:
  out.append(num**2)
print(out)

out = [num**2 for num in x]
```

## Functions

Syntax:

```
def my_func(param1="default"):
  '''
  This is doctstring
  '''
  return "Printing function {}".format(param1)

print(my_func("hello"))
```

### Lambda expressions

```
mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
  return num % 2 != 0
evens = filter(even_bool, mylist) #filter is a generator
print(list(evens))

evens = filter(lambda num: num%2 == 0, mylist)
print(list(evens))
```

### Methods

st = "Hello"

- st.lower()
- st.upper()
- st.split()

### Scope

- Python Scope follow the LEGB Rule:
  - Local
    - Names assigned in any way within a function (def or lambda), and not declared global in that function.
  - Enclosing Function locals
    - Names in the local scope of any and all enclosing functions (def or lambda), from iiner to outer.
  - Global
    - Names assigned at the top-level of a module file, or delcared global in a def withing the file.
  - Built-in
    - Names preassigned in the built-in names module: open, range, SyntaxError,...

## Object Oriented Programming

- In Python everything is object
  - To check: print(type(20.0)) # class 'float'
- We create our own objects with classes

```
class Sample():
  pass

x = Sample()
print(type(x)) # <class '__main__.Sample>
```

- Special methods

```
#string representation special method
  def __str__(self):
    return f'Title: {self.title}, Author: {self.author}, Pages: {self.pages}'

# len method
  def __len__(self):
    return self.pages

# delete method
  def __del__(self):
    print("a book has been destroyed")
```

### Errors and Exceptions

- We can use these keywords to dictate our code logic in case of an error:
  - Try
  - Except
  - Finally

### Handy tools

- To open files use the open() function
  - open("myfile.txt","r")
  - The second parameter in the open() function dictates whether you are opening the file or just reading, just writing, or to do both
  - If you use the wrong one , you may get an error

## Regular Expressions

- Allow us to search for patterns in Python strings
- import re
  ex.

  ```
  text = 'This is a string with term1 in it'
  if re.search(pattern,text):
    print("match')

  match = re.search('term1', text)
  print("match",match.start()) # match 22 -> finds the match at line 22
  ```

  We can use split with REX

```
split_term = '@'
email = 'user@gmail.com'

print(re.split(split_term, email)) # ['user', 'gmail.com']
```

To find all the instances of a pattern:

```
re.findall('match', 'test phrase match in the middle) # ['match']
```

## Decorators

- Decorators are an advanced tool in Python
  ex.:

```
def new_decorator(func):

  def wrap_func():
    print("code before executing func")
    func()
    print('func() has been called')
  return wrap_func

# with decorator
@new_decorator
def func_needs_decorator():
  print('This function is in need of a decorator')

'''
without decorator:
func_needs_decorator = new_decorator(func_needs_decorator)
'''

func_needs_decorator()
```
