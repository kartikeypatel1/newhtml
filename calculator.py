num1=int(input("enter the first number:"))
num2=int(input("enter  the second number:"))
operator=input("enter a operator:")
match operator:
    case "+":
        print(num1+num2,"addition is performed")
    case  "-":
        print(num1-num2,"subtraction is performed")
    case "/" :
        print(num1/num2,"division is performed")
    case "*":
        print(num1*num2,"numltiplication is performed")
    case "**":
        print(num1**num2,"power is performed")
    case "//":
        print(num1//num2,"floor division is performed  ")
    case _:
        print("enter a valid operator")                      