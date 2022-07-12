#1부터 n까지의 곱을 구하여 출력하는 코드를 
# 1) while 문 2) for 문으로 각각 작성하시오.

#while문
n = int(input())
i = 0
sum = 1
while i<n:
    i += 1
    sum = sum * i    
print(sum)

#for문
n = int(input())
i = 0
sum = 1
for i in range(n):
    i += 1
    sum = sum * i
print(sum)

