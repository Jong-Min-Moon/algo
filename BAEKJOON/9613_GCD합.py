def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

#'가능한 모든 조합' = for loop 2번.
for _ in range(int(input())):
    N, *arr = map(int, input().split())
    # 숫자 하나만 입력하면 N만 채워지고, arr은 빈 리스트가 됨.
    # 리스트가 안 생기는게 아니라 빈 리스트가 arr에 할당된다는 것 주의.
    sum_GCD = 0
    for i in range(N-1):
        a = arr[i]
        for j in range(i+1, N):
            b = arr[j]
            #print('calculate GCD of %d and %d' %(a,b) )
            sum_GCD += gcd(a, b)
    print(sum_GCD)
