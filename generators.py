import random

def lottery():
  for i in range(6):
    yield random.randint(1,40)
  yield random.randint(1,15)

for random_number in lottery():
  print("Next number is %d" % random_number)

print("Exercise")
a = 1
b = 2
a, b = b, a
print(a,b)

# fill in this function
def fib():
  a = 0
  b = 1
  while(True):
    a, b = b, a + b 
    yield a  

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
