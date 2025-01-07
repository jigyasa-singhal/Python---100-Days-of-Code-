# strings methods 

name = 'Harry.......'

name1="hello world"

# by for loop acessing the strings

for i in name :

    print(i)

   

# len() it counts the length of the strings

print("Length of the string is : " ,len(name))

 

print(name.upper())

print(name.lower())

#rstrip removes the last given char

print(name.rstrip("."))

#strip Remove the space before the strings

print(name.strip())

#replace the given element with the given element

print(name.replace(".","a"))

#split helps to split the string from the given element and returns to it in the list

print(name1.split(" "))

# Capitalise returns the first letter of the strings to be upper case and rest to be the lowercase

print(name1.capitalize())

# center method aligns the string to the center

print(name1.center(25,"*"))

# count returns the given char is to be count

print("The no. of occurences in the strings :  " ,name1.count("l"))

# endswith() if strings ends with  the    given element it returns true otherwise false

# startswith() check in the start

print("is ends with ",name1.endswith("@"))

print("is the starts with : ", name1.startswith("he"))

 

# finds() return the first index of the given char if not present return -1

print(name1.find("l"))

# isalnum () it returns the. true if the string is contain aplhabhets can be lowercase or upper case  or numeric

name1="hello world"

 

print(name1.isalnum())

# isaplha () it returns true when the given strings is only contains aplhabhets

print(name1.isalpha()) # returns false space present their

 

# islower() it returns true  if the given strings is lowercase  

print(name1.islower())

# isupper() it returns true  if the given strings is uppercase

print(name1.isupper())

#isprintable it returns true if all elements of the strings is printable

str1 = "Hello/n"

print("It is printable ", name1.isprintable()) #true

print("it is not printable",str1.isprintable()) #false = /n is not printble

#isspace() it returns true if strings contains the white space

print(name1.isspace())

# swapcase(): it turns lower case of the strings to upper case and vice versa.

name1="hello world"

print(name1.swapcase())







 

 