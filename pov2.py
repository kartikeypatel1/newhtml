num=int(input("enter the integer"))
if (num%5==0 or num%3==0) and num%15!=0:
    print(num,"not divisible by 15")
else:
    print(num,"number is divisible by 15 ")    