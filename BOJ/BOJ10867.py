N = int(input())

list_ = list(map(int,input().split()))
result = list(set(list_))
result.sort()
print(*result)