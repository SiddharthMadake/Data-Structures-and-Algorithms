def max_num(arr):
    a1=arr[0]
    
    for x in arr:
        if x > a1:
            a1 = x
    return a1

arr = [1,23,459,22,34,98,34,66,87]

print(max_num(arr))