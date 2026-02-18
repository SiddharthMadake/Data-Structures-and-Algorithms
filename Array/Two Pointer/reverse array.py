def rev_array(arr):
    left=0
    right=len(arr) - 1
    
    while left < right:
        
        arr[left],arr[right] =  arr[right] , arr[left]
        
        left += 1
        right -= 1
        
    return arr

arr = [1,2,3,4,5,6,7,8,9]

print(rev_array(arr))