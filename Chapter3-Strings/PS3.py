#  Write a program to detect double space in a string.
# name="Anjum is a good girl and"    ---if o/p is  -1 , it does not have double string 

name="Anjum is a good  girl and"    #if o/p is  15 [index], it have double string
print(name.find("  "))