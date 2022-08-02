A, B = map(int,input().split())

N = list(map(int,input().split()))
M = list(map(int,input().split()))
result = []
X = len(N) + len(M)
for i in N:
    if i in M:
        result.append(i)
ans = X - (len(result) * 2)
print(ans)
