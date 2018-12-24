def outer_func(message):
  def nested_func():
    nonlocal message
    message = 3
    print(message)
  nested_func()
  print(message)
message = 9
outer_func(message)
print(message)


def messager(message):
  def nested_messager():
    print(message)
  return nested_messager

func1 = messager("Hello")
func1()

def counter(value):
  def increment():
    nonlocal value
    value+=1
    return value
  return increment

func2 = counter(5)
print(func2())
print(func2())
print(func2())
print(func2())

def multiplier_of(first):
  def multiplier(second):
    return first * second
  return multiplier

multiplywith5 = multiplier_of(5)
print(multiplywith5(9))

