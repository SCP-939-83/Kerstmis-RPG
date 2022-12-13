class MyClass:
  x = "cheese"

p1 = MyClass()
print(p1.x)

class Person:
  def __init__(self, name, age, level):
    self.name = name
    self.age = age
    self.level = level

p1 = Person("John", 36)

print(p1.name)
print(p1.age)