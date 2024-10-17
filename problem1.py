eng_marks=int(input("enter the english marks:"))
math_marks=int(input("enter the maaath marks:"))
if eng_marks>80 and math_marks>80:
    print("A+")
elif eng_marks>80 and math_marks<80 or eng_marks<80 and math_marks>80:
    print("B")
else:
    print("C")        