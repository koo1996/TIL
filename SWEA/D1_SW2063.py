N = int(input())

number = list(map(int,input().split()))
result = sorted(number)
print(result[N//2])