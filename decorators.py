def repeater(old_func):
  def new_func(*args, **kwds):
    old_func(*args, **kwds)
    old_func(*args, **kwds)
  return new_func

@repeater
def multiply(num1, num2):
  print(num1 * num2)

multiply(2,3)

def double_out(old_func):
  def new_func(arg):
    if arg < 0: raise ValueError("Negative Argument")
    return 2 * old_func(arg * 2)
  return new_func

@double_out
def foo(val):
  return val;

print(foo(2))

def multiply(multiplier):
  def multiply_generator(old_func):
    def new_func(*args, **kwrds): 
      return multiplier * old_func(*args, **kwrds)
    return new_func
  return multiply_generator

@multiply(3)
def return_num(num):
  return num
print(return_num(3))


def type_check(correct_type):
  def checker(old_func):
    def new_func(arg):
      if (isinstance(arg, correct_type)):
         return old_func(arg)
      else:
         print("Bad Type")
    return new_func;
  return checker  

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])
