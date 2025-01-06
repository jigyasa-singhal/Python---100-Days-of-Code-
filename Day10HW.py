# without typecasting the input
'''
a = input("enter the number 1 :")                   # input = 12 
b = input("enter the number 2 : ")                  # input = 12 
print(f"addition of a {a} and {b} is ",a+b)         # output = 1212
print(f"subtraction of a {a} and {b} is ",a-b)      # output = error 
print(f"multiplication of a {a} and {b} is ",a*b)   # output = error
print(f"dividion  of a {a} and {b} is ",a/b)        # output = error
'''
# with typecast the input 
c = int (input("enter the number 1 :"))             # input = 12 
d = int (input("enter the number 2 : "))            # input = 12 
print(f"addition of a {c} and {d} is ",c+d)         # output = 1212
print(f"subtraction of a {c} and {d} is ",c-d)      # output = 0 
print(f"multiplication of a {c} and {d} is ",c*d)   # output = 144
print(f"dividion  of a {c} and {d} is ",c/d)        # output = 1.0



