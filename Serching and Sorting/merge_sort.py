def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right =  merge_sort(a[mid:])
    return merge(left,right)

def merge(left,right):
    res=[]
    i=j=0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

print(merge_sort([2,5,3,7,1,4,9]))
