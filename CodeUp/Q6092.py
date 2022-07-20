list_name=list()

for i in range(23):
    list_name.append(0)

N = int(input())
number = list(map(int,input().split()))

for test in range(N):
     list_name[number[test]-1] += 1

print(*list_name, end=' ')
