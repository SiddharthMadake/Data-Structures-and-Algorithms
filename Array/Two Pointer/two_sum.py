def two_sum(arr,target):
    left=0
    right = len(arr) -1
    
    while left < right:
        current = arr[left] + arr[right]
        
        if current == target :
            return left, right
        elif current < target:
            left += 1
        else:
            right -= 1
    return -1
 
a= [1,2,3,4,6,7]
b= 13
            
if __name__ == "__main__":
   print( two_sum(a,b))