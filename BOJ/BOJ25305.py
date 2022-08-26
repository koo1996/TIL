N,M = map(int,input().split())
Number = list(map(int,input().split()))
Number.sort(reverse=True)
result = []

for j in range(M):
    result.append(Number[j])
print(min(result))