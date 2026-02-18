def pal(arr):
    left = 0 
    right = len(arr) - 1
    
    while left < right:
        
        if arr[left] != arr[right]:
            return False
        left +=1
        right -= 1
    return True

arr = [1,2,3,4,5,5,4,3,2,1]



if __name__ == "__main__" :
    if pal(arr):
        print("palindrome")      
    else:
        print("not palindrome")        