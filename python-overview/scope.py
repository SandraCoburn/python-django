x = 25
def my_func():
  x = 50
  return x
print(x) # 25
print(my_func()) #50
my_func()
print(x) #25

# local level
lambda x: x**2

# Enclosing funtion locals
name = "This is a global name"

def greet():
  #name = "Sammy"
  def hello():
    print('hello '+ name)
  hello()
print(greet())
#Build into level

# To change global variable -> not reccomended
def func():
    global x
    x = 100
print("before function call, x is:", x)#25
func()
print('after function call, x is: ',x) #100