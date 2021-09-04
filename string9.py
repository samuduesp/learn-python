my_str ="testing"
my_str.capitalize()
id(my_str)
id("testing")
other_str = "testing"
id(my_str) == id(other_str) #true
len(my_str) #numbers of characters
test_string = "testing"
test_string[0]
test_string[-1]
test_string[0:2]
test_string[3:len(test_string)]
test_string[3:] #can get all index after 3

test_string[1:6:2] #slicing ==stepping numbers and get value
                           # ==last number how many items you going to jump
test_string[:6:2]   #starting by 0
test_string[1::2]
test_string[::-1]  #this is like reversing ---gnitsetmy.