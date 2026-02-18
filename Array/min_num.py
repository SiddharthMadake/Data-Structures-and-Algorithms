def min_num(arr):
    a1= arr[0]
    
    for x in arr:
        if x < a1 :
            a1 = x
            
    return a1

arr = [81,243,459,220,34,98,384,66,87]
print(min_num(arr))        