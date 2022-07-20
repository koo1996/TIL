N = int(input())

for test in range(0,N+1): #N번 반복
    result = 2 ** test #2^0 ~ 2^N 번까지 출력
    print(result, end=' ')