a=int(input("enter first num:"))
b=int(input("enter first num:"))
c=[]

for i in range(a,b+1):
    if i <= 1:
        continue
    for j in range(2,int(i*0.5)+1):
        if i % j ==0:
            break
    else:
            c.append(i)
print(c)
print("count is",len(c))