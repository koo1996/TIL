N = input()
list_ = [0 for _ in range(26)]

for i in range(len(N)):
    M = ord(N[i]) - 96
    list_[M-1] += 1
print(*list_)