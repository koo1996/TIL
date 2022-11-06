list=[i for i in range(1,31)]
for i in range(28):
    N = int(input())
    list.remove(N)
print(min(list))
print(max(list))
    