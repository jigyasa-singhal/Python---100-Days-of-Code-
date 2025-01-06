num1= int(input("Enter the number 1 "))
num2= int(input("Enter the number 2 :"))
work = input("Enter the operator")

match work:
    case "+":
        print(f"The addition of {num1} and {num2} is : \n")
        print(num1+num2)
    case"-":
        print(f"The subtraction of {num1} and {num2} is : \n")
        print(num1-num2)
    case"*":
        print(f"The mulltiplication of {num1} and {num2} is : \n")
        print(num1*num2)
    case"/":
        print(f"The division of {num1} and {num2} is : \n")
        print(num1/num2)
    case"**":
        print(f"The exponential of {num1} and {num2} is : \n")
        print(num1**num2)
    case"//":
        print(f"The floor division  of {num1} and {num2} is : \n")
        print(num1//num2)