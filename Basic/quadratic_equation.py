a=int(input("enter a num "))
b=int(input("enter b num "))
c=int(input("enter c num "))

d= (b*b - (4*a*c)) ** 0.5
if a==0:
    print("a is not zero possible")
elif d < 0:
    print("root is imaginary")
elif d == 0:
    t=-b/(2*a)
    print("root",t)
else:
    q=(-b+d)/(2*a)
    w=(-b-d)/(2*a)
    print(f"root1 is {q} and root2 is {w}")