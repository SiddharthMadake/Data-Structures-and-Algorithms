a=int(input("enter a number:"))
flage=True

if a <= 0:
    print("enter positive num ")

elif a == 1:
    print(f"{a} is not prime num")
    print(f"{a} is not prime num")
else:
    for i in range(2,int(a**0.5)+1):
        if a % i ==0:
            flage = False
            break
         
if flage:
    print(f"{a} is prime num")
else:
    print(f"{a} is not prime num")