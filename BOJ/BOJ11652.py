N = int(input())
dict = {}
for i in range(N):
    A = int(input())
    if A not in dict:
        dict[A] = 1
    else:
        dict[A] += 1
dict = sorted(dict.items(), key=lambda x: (-x[1], x[0]))
print(dict[0][0])
