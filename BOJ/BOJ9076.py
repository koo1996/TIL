T = int(input())

for _ in range(T):
    M = list(map(int,input().split()))
    M.remove(max(M))
    M.remove(min(M))
    if max(M) - min(M) >= 4:
        print('KIN')
    else:
        print(sum(M))