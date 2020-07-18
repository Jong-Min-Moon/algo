#my code
def ins_sort(a):
    n = len(a)
    for i in range(1, n):
        mover = a[i]
        presorted = a[ : i]

        #find the right place
        for j in range(i):
            if mover < presorted[j]:
                temp = presorted[j: ]
                print(temp, 'moved one step to the right')
                a[j] = mover
                a[j+1 : i+1] = temp
                break

        print(a)

d = [4,2,5,6,3,1]
ins_sort(d)
print('\n')

#book
def ins_sort2(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i-1
        while j>=0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
        print(a)

d = [2,4,5,1,3]
ins_sort2(d)