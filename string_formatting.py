mylist = [1,2,3]
print("List value is %s" % mylist)

myint = 1321
print("Integer is %d" % myint)
print("Integer in hex %X" % myint)

myfloat = 5.4321
print("Float is %f" % myfloat)
print("Float with fixed ammount of digits(2) is %.2f" % myfloat)

print("Exercise")
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%.2f"

print(format_string % data)
