#lab5_conditionals

value = int(input("enter the integer value: "))

if value % 5 == 0 and value % 3 == 0:
    print("fizzbuzz")
elif value % 5 == 0:
    print("fizz")
elif value % 3 ==0 :
    print("buzz")
else:
    print("value")

