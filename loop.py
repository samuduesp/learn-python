while 1 < 2:
    print("something") #print forever if  condition is correct

count = 1
while count <= 4:
    print("looping")
    count += 1

name = ["blue", "green", "red", "yellow"] 
for colour in name:
    print(colour)

point =(1,2,3)
for numbers in point:
    print(numbers)

ages ={"kevin":12, "bob":23, "dollu":4}
for name,value in ages.items():
    print(name,value)

#nesting_loops

counter = 8
while counter  <= 25:
    if counter % 4 == 0:
        print(counter)
    counter += 1

#controling loop excution
#continue
#break
#

count = 0
while count <= 10:
    if count % 2 == 0:
        count += 1
        continue
    print(f"we are counting odd numbers: {count}")
    count +=  1

count = 1
while count < 10:
    if count % 2 == 0:
        break
    print(f"we are counting odd numbers: {count}")
    count +=  1

colours =['red','green','blue']   
for i in colours:
    if i == 'green':
        print("orange is not in the list")
        break
else:
    print("orange is not in the  list")


for i in range(4):
    print("looping")

colors = ["red", "green", "blue", "black"]

upper_color = []

for color in colors:
    upper_color.append(color.upper())

upper_color=[color.upper() for color in colors ]
warm_color = [color for color in colors if color in ["red", "blue"]]