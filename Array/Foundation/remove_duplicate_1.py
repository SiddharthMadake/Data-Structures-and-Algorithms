a=[2,3,4,4,3,5,6,7,3,4,8,9]
a.sort()

def remove(a):
    b=[a[0]]
    for i in range(1,len(a)):
        if a[i]!=a[i-1]:
            b.append(a[i])
    return b
print(remove(a))