N = int(input())
list_1 = []
for i in range(N):
    M = int(input())
    list_1.append(M)
list_1.pop(max(list_1)-1)
print(list_1)