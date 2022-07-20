N = int(input())
number = list(map(int,input().split()))

result = []
for i in range(N-1,-1,-1):
    result.append(number[i])
print(*result)