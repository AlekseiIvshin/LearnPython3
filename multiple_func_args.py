def foo(first, second, third, *rest):
  print("First: %s" % first)
  print("Second: %s" % second)
  print("Third: %s" % third)
  print("All the rest: %s" % list(rest))

foo("Answer to", "the Ultimate Question of Life", "the Universe", "and", "Everything")


def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))

print("Exercise")
# edit the functions prototype and implementation
def foo(a, b, c, *therest):
  return len(list(therest))
  
def bar(a, b, c, **options):
  return options["magicnumber"] == 7


# test code
if foo(1,2,3,4) == 1:
    print("Good.")
if foo(1,2,3,4,5) == 2:
    print("Better.")
if bar(1,2,3,magicnumber = 6) == False:
    print("Great.")
if bar(1,2,3,magicnumber = 7) == True:
    print("Awesome!")
