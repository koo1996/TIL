C = int(input())
for _ in range(C):
    N = list(map(int,input().split()))
    sum = 0
    count = 0
    for i in range(1,len(N)):
        sum += N[i]
    avg = sum / N[0]
    for j in range(1,len(N)):
        if N[j] > avg:
            count += 1
    result = (count / N[0]) * 100
    print(format(result,".3f"),'%',sep='')

