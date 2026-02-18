arr=[9,8,7,6,5,4,3,2,1]
def a(arr):
    left=0
    right=len(arr) - 1
    
    while left < right :
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

print(a(arr))
