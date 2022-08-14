N = [1,1,2,2,2,8]

M = list(map(int,input().split()))
for i in range(len(M)):
    print(N[i] - M[i],end=' ')