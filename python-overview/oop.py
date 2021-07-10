class Sample():
 
    pass

x = Sample()
print(type(x)) # <class '__main__.Sample>

class Dog():
  #Class object attributes
  species = "mammal"

  #methods
  def __init__(self,breed, name):
    self.breed = breed
    self.name = name

mydog = Dog('Lab', "Anabel")
# otherdog = Dog(breed = 'Huskie')
print(mydog.breed)
print(mydog.name)
print(mydog.species)

class Circle():
  pi = 3.14

  def __init__(self,radius):
    self.radius = radius
  
  def area(self):
    return self.radius * self.radius * Circle.pi

  #method to reset object's attribute
  def set_radius(self, new_r):
    self.radius = new_r

myc = Circle(20)
print(myc.area()) #1256.0
myc.radius = 100
print(myc.area())
myc.set_radius(80)
print(myc.area())

## INHERITANCE
class Animal():

  def __init__(self):
    print("Animal Created")

  def whoAmI(self):
    print("Animal")

  def eat(self):
    print("Eating")


class Dog(Animal):
  def __init__(self):
    Animal.__init__(self)
    print("Dog created")
  
  def bark(self):
    print("wolf")

# myanimal = Animal()
# myanimal.whoAmI()
# myanimal.eat()

myDog = Dog()
myDog.whoAmI()
myDog.eat()

## SPECIAL METHODS

class Book():
  def __init__(self, title,author,pages):
    self.title = title
    self.author = author
    self.pages = pages
#string representation special method
  def __str__(self):
    return f'Title: {self.title}, Author: {self.author}, Pages: {self.pages}'

# len method
  def __len__(self):
    return self.pages

# delete method
  def __del__(self):
    print("a book has been destroyed")


mybook = Book("Python", "author", 200)
print(mybook)
mylist = [1.2,3]
print(len(mybook))
del mybook # removes mybook from memory and returns "a book has been destroyed"