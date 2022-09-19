N = int(input())

for i in range(1,N+1):
    M = list(map(int,input().split()))
    Max_ = max(M)
    Min_ = min(M)
    result = (sum(M) - (Max_+Min_)) / (len(M) - 2)
    print(f'#{i}',round(result))