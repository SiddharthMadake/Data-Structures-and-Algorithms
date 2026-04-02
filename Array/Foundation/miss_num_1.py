a=[1,2,3,4,6,7,8,9]
a.sort()

def miss(a):
    for i in range(1,len(a)+1):
        if i != a[i-1]:
            print("missing",i)
            return
miss(a)
