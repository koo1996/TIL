#1부터 그 수까지 짝수만 합해 출력한다.

n = int(input())
sum = 0
for i in range(n+1):
    if i % 2 == 0:
        sum = sum + i
print(sum)