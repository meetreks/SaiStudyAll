#!/usr/bin/env python
import collections
import sys
#If you have a list, tupple, array etc of Data and if you would like to run a function against that data then map is ideal
# In the first example you see that we pass a lambada function which takes a int and provides a sqare of that integer
# from the list of the arrays passed
# In the Second Example, you can see that we take a tuple and convert the second element of the tuple with an arithemetic
# operation function
#filter can in a similar way filter data and give you what you want. Like the map function, the result is a object so always
#use a list function to traverse through the returned object.

def five(x): return 5
print(map(five,[1,2,3]))

print(list(map(lambda x: x **2,[1,2,3])))
temps = [("Berlin", 29),("Paris", 39),("London", 19),("Madrid", 39),("Monaco", 49)]
c_to_f = lambda data: (data[0], (9/5) * data[1]+ 32)
print(list(map(c_to_f,temps)))
word0 = [("a"),("b"),("c"),("a")]
map_to_word = list(filter(lambda x: x == x,word0))
print(map_to_word)