T = int(input())
for j in range(1,T+1):
    N = int(input())
    list_ = [50000,10000,5000,1000,500,100,50,10]
    result = []
    for i in range(len(list_)):
        res = N // list_[i]
        result.append(res)
        N -= res * list_[i]
    print(f'#{j}')
    print(*result)