import sys
input = sys.stdin.readline

n = int(input())

list = []
for i in range(n):
    [a,b] = map(int,input().split())
    list.append([a,b])

result = sorted(list)

for j in range(n):
    print(result[j][0], result[j][1])
