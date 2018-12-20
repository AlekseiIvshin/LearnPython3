def my_func():
  print("Hello from my func")

def say_hello(username, greeting):
  print("Hello, %s! I wish you %s"%(username, greeting))

def sum_two_numbers(a,b):
  return a + b

my_func()
say_hello('John', 'death')
print(sum_two_numbers(1,2))

print("Exercise")

# Modify this function to return a list of strings as defined above
def list_benefits():
  return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
  return benefit + " is a benefit of functions!"

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
