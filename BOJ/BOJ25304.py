N = int(input())
sum = 0
for i in range(int(input())):
    A, B = map(int,input().split())
    sum += A * B
if N == sum:
    print('Yes')
else: 
    print('No')