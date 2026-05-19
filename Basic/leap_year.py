a=int(input("enter year:"))

if a % 400 == 0 :
    print(f"{a} is leap year")
elif a % 4 ==0 and a % 100 != 0:
    print(f"{a} is leap year")
else:
    print(f"{a} is not leap year")