f = open("demofile.txt")


#open fle different location
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())

#reads only parts of the file
f = open("demofile.txt", "r")
print(f.read(5))

#close file
f = open("demofile.txt", "r")
print(f.readline())
f.close()

#append
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

#create a neww file
f = open("myfile.txt", "x")


#remove the file
import os
os.remove("demofile.txt")

#check before file exist
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

#remove folder
import os
os.rmdir("myfolder")

