def e_f():
    a=int(input("Enter a Num:"))
    i,j=1,2
    total=0
    while i <= a:
        if i % 2 == 0:
            total+=i
        i,j=j,i+j
    print(total)
e_f()