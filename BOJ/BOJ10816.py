import sys
input = sys.stdin.readline

N = int(input())
Numbers = list(map(int,input().split()))
M = int(input())
F_Numbers = list(map(int,input().split()))

result = []
for i in range(len(F_Numbers)):
    cnt = 0
    for j in range(len(Numbers)):
        if F_Numbers[i] == Numbers[j]:
            cnt += 1
    result.append(cnt)
print(*result)