T = int(input())

for i in range(T):
    N = list(input())
    res = 0
    for j in range(len(N)):
        cnt = N.count(j)
        for k in range(j+1,len(N)):
            if N[j] == N[j+1]:
                res += 1
            else:
                res = 0
        
            if cnt != res:


        