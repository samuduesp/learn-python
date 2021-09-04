name = input('what is your name ?')
color = input('what is your favourite colour ?') 
age = input(' what is your age?')
'''
print(name, end=" " )
print('is ' + str(age) + ' years old', end=" ")
print("and loves the color " +  color + ".")
'''


print(name, "is", age, "years old and loves the color", color + ".")

print(name, "is", age, "years old and loves the color", color + "." , sep=", ")

