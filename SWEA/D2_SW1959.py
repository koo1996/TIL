T = int(input())
for test in range(1,T+1):
    A,B = map(int,input().split())
    X = list(map(int,input().split()))
    Y = list(map(int,input().split()))
    for i in range(A):
        for j in range(i+1,)