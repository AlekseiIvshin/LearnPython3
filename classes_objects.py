class MyClass:
  variable = "ba da bum tss"

  def function(self):
    print("Message is inside the class")

myobj = MyClass()
print(myobj.variable)
myobj.function()

print("Exercise")

class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here

car1 = Vehicle()
car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000.0

car2 = Vehicle()
car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000.0

# test code
print(car1.description())
print(car2.description())

class Spell:
  def __init__(self):
    self.name = "Not defined yet"
  def set_name(self, new_name):
    self.name = new_name

spell = Spell()
print(spell.name)
spell.set_name("Workious")
print(spell.name)
