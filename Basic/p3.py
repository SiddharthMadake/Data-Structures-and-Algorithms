
a=int(input("enter number"))
b=str(a)
c=len(b)
s_p=0
while a > 0:
        d=a%10
        s_p+=d ** c
        d=a//10
if a == s_p:
        print("armstrong")
else:
        print("not armstrong")