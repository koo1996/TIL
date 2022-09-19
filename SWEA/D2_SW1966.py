N = int(input())

for i in range(1,N+1):
    M = int(input())
    list_ = list(map(int,input().split()))
    list_.sort()
    print(f'#{i}',*list_)