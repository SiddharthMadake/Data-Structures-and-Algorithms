def array_sum(arr):
    s = 0
    for x in arr:
        s += x
    return s

arr = [1,23,459,22,34,98,34,66,87]

print(array_sum(arr))