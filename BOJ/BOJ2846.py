N = int(input())
Size_ = list(map(int,input().split()))
result = []
cnt = 0
for test_1 in range(1,N):
    if Size_[test_1] > Size_[test_1 - 1]:
        X = Size_[test_1] - Size_[test_1 - 1]
        cnt = cnt + X
        if test_1 == N:
            result.append(cnt)
    else:
        cnt = 0
        result.append(cnt)
print(result)
