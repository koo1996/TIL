T = int(input())

for _ in range(T):
    result = []
    A,B = input().split()     
    for i in range(len(B)):
        sum = 0
        sum = B[i] * int(A)
        result.append(sum)
    print(*result,sep='')