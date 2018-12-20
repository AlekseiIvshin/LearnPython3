phonebook = {
  "John" : 123,
  "Jack" : 456,
  "Jill" : 789
}
print(phonebook)

print(phonebook.pop("Jack"))

for name, number in phonebook.items():
  print("Phone number of %s is %d" % (name, number))

print("Exercise")

phonebook1 = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# write your code here
phonebook1["Jake"] = 67859430
del phonebook1["Jill"]

# testing code
if "Jake" in phonebook1:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook1:
    print("Jill is not listed in the phonebook.")
