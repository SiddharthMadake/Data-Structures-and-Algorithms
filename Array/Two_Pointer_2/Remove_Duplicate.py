a=[1,1,2,2,2,3,5,5,6,2]
a.sort()

def dup(a):
    if not a:
        return 0
    slow=0
    for fast in range(1,len(a)):
        if a[slow] != a[fast]:
            slow+=1
            a[slow]=a[fast]
    return slow + 1

length = dup(a)

print(a[:length])