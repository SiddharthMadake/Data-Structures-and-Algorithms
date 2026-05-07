def p1():
    a=int(input("enter last num:"))
    b=int(input("first multiple:"))
    c=int(input("second multiple:"))
    d=[]
    e=[]
    s=0
    for i in range(1,a):
        if i % b == 0:
            d.append(i)
        elif i % c == 0:
            e.append(i)
    f=d+e
    j=set(f)
    h=list(j)
    
    for q in h:
        s+=q
        
    print(s)
p1()