T = int(input())

final_ = 0
for i in range(T):
    N = input()
    res = 0
    for j in range(len(N)-1):
        if N[j] != N[j+1]:
            M = N[j+1:]
            if M.count(N[j]) > 0:
                res += 1
    if res == 0:
        final_ += 1
print(final_)