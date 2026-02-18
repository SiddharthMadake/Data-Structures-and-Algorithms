def e_o_count(arr):
    e=o=0
    for x in (arr):
        if x % 2 == 0:
            e += 1
        else:
            o +=1
    return e,o


arr = [81,243,459,220,34,98,384,66,87]
print(e_o_count(arr))        