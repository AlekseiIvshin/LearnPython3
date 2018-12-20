print("Practice")

name = "John"
age = 23
if name == "John" and age == 23:
  print("I found you John Conor!")

if name == "John" or name == "Rick":
  print("Hmm, you are John or Rick")

if name in ["John", "Rick"]:
  print("Hmm, you are John or Rick")

if name == "Rick":
  print("Wubbalubbadubdub!")
elif name == "John":
  print("Here's Johny!!!")
else: 
  print("There are not anybody")

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

print(not False)
print((not False) == (False))

print("Exercise")

# change this code
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [2,3]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
