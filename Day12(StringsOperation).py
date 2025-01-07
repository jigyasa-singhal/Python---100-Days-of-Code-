#slicing operations on the strings

s="Python"
#print(s[:::])            #output = Python
print(s[::-1])            #output = nohtyP
print(s[-2:])             #output = on
print (s[-3:-1])          #output = ho
print(s[0:6])             #output= Python

lst = [10, 20, 30, 40, 50]
print(lst[4::-1])   #[50, 40, 30, 20, 10]

print(lst[-3:-1])   #[30, 40]
print(lst[::2 ])    #[10, 30, 50]
print(lst[::-2])    #[50, 30, 10]