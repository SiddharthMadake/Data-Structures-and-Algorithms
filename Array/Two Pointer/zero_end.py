def zero_end(arr):
    slow= 0
    l1=[]
    for fast in range(len(arr)):

        if arr[fast] != 0:
            l1.append(arr[fast])
        else:
            slow +=1
    return l1 + [0] * slow
            
arr = [1,20,3,4,0,5,0,55,30,0,1]

if __name__ == "__main__":
    print(zero_end(arr))