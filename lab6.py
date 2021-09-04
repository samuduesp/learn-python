number =int(input("how many values should we process: "))


"""
for value in range(1,number+1):
   #print(value)
   if((value % 3 == 0) and (value % 5 == 0)):
       print("fizzbuzz")
   elif(value % 3 ==  0):
       print("fizz")
   elif(value % 5 == 0):
       print("bizz")
   else:
       print(value)
"""

count = 1
while count <= number:
    if((count % 3 == 0) and (count % 5 == 0)):
        print("fizzbuzz")
    elif(count % 3 ==  0):
        print("fizz")
    elif(count % 5 == 0):
        print("bizz")
    else:
        print(count)
    count +=1

    

