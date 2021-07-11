s = "Global Variable"
def func():
  s=50
  print(locals()) #will print all local variables in a dictionary
  print(globals()['s']) # will print 'Global Variable'
  return s

print(func())

def hello(name='Jack'):
  return "hello "+ name

print("hello",hello())

## Assign a label to a function
mynewgreet = hello
print("mynewgreet",mynewgreet())

## Functions within functions
def greetings(name="Sean"):
  print("The greetings() function has been run!")

  def hello():
    return "This string is inside hello()"

  def welcome():
    return "This string is inside welcome"

  # print(hello())
  # print(welcome())
  # print('End of hello()')

  ## Returning functions
  if name == "Sean":
    return hello
  else:
    return welcome

x = greetings()
print(x())

# Function as an argument
def greet():
  return 'Hi Jack!'

def other(func):
  print("hello")
  print(func())
 
other(greet)

#  Decorators
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