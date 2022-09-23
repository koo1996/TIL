N = int(input())

Time_ = list(map(int,input().split()))
Time_.sort()
sum_ = 0
result = []
for i in range(N):
    sum_ += Time_[i]
    result.append(sum_)
print(sum(result))
