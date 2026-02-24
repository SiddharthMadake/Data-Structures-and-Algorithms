b=[5,3,7,5,2,7,8,2]
a=[1,2,3,4,5,6,7]
def sort_a(a):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return False
    
    return True
    
if sort_a(b):
    print("yes")
else:
    print("no")