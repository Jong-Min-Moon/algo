def find_ins_idx(r,v):
    #find the right place for v in a pre-sorted list r
    n = len(r)
    for i in range(n):
        if v < r[i]:
            return i
    return n #v is larger than all elements of r

def ins_sort(a):
    result = []
    while a:
        value = a.pop(0)
        ins_idx = find_ins_idx(result, value)
        result.insert(ins_idx, value)
        print(a, result)
    return result

d = [1,3,5,2,4]
print(ins_sort(d))
