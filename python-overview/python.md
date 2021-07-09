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