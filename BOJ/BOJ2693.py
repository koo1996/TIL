T = int(input())

for _ in range(T):
    M = list(map(int,input().split()))
    M.sort()
    print(M[7])