a=int(input("enter num:"))
b=1
if a== 0 :
    print("factorial of 0 is 1")
else:
    for i in range(1,a+1):
     b*=i
print(b)