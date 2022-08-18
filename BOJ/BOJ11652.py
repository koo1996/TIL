N = int(input())
dict = {}
for i in range(N):
    A = input()
    if A not in dict:
        dict[A] = 1
    else:
        dict[A] += 1
M = max(dict,key=dict.get)
print(min(M))
