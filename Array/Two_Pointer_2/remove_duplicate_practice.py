def r_d(a):
    slow=0
    for fast in  range(len(a)):
        if a[fast] != a[slow]:
            slow += 1
            a[slow]=a[fast]
            
    return slow + 1
a=[1,1,2,3,4,4,4,5,6,6]
k = r_d(a)
print(a[:k])