class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

class Person:
  def __init__(self, name, age, level):
    self.name = name
    self.age = age
    self.level = level
x = 5
y = 1
p1 = Person("John", x, y)
print(p1.name)
print(p1.age)
print(p1.level)

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()