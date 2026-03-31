a=[2,4,5,67,7,8,9]

def is_sort(a):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return False
    return True
if is_sort(a):
    print("sorted")
else:
    print("not sorted")