# https://www.acmicpc.net/problem/2577

a = int(input())
b = int(input())
c = int(input())
result = a * b * c
list_1 = []
for test_1 in str(result):
    list_1.append(test_1)

list_2 = [0 for i in range(0,10)]

for test_2 in range(0,len(str(result))):
    list_2[int(list_1[test_2])] += 1
print(*list_2, sep='\n')
