#####################################
#### PART 6: EXERCISE REVIEW  #######
#####################################

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

###############
## Problem 1 ##
###############

# Given the string:
s = 'django'

# Use indexing to print out the following:
# 'd'
print(s[0])
# 'o'
print(s[-1])
# 'djan'
print(s[0:4])
# 'jan'
print(s[1:4])
# 'go'
print(s[4:])
# Bonus: Use indexing to reverse the string
print(s[::-1])

###############
## Problem 2 ##
###############

# Given this nested list:
l = [3,7,[1,4,'hello']]
# Reassign "hello" to be "goodbye"
l[2][2] = "goodbye"
print(l)

###############
## Problem 3 ##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}
print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}
print(d2["k1"]["k2"])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3["k1"][0]["nest_key"][1][0])

###############
## Problem 4 ##
###############

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
newSet = set(mylist)
print(newSet)

###############
## Problem 5 ##
###############

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"
print("Hello my dog's name is {name} and he is {age} years old".format(name="Sammy", age=4))

#Tuples
mypairs = [(1,2),(3,4),(5,6)]

for(tup1, tup2) in mypairs:
  print(tup1) # will print all the numbers 1,2,3,
  print(tup2) # will print all the numbers 4,5,6

# Range is a generator
l = [1,2,3,4,5]
print(range(5)) # range(0,5)
print(list(range(0,5))) # [0,1,2,3,4] 
print(list(range(0,20,2))) # [0,2,4,6,8,10,12,14,16,18]

#list comprehension
x = [1,2,3,4]
out = []
for num in x:
  out.append(num**2)
print(out)

out = [num**2 for num in x]
print(out)