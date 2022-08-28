from re import M


N = int(input())

result = [0, 1]
for i in range(2,N+1):
    num = result[i-1] + result[i-2]
    result.append(num)
print(result[N])