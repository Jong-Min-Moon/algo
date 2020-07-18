#book
def ins_sort_desc(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i-1
        while j>=0 and a[j] < key:#changed here. stop when he faces someone larger.
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
        print(a)

d = [2,4,5,1,3]
ins_sort_desc(d)