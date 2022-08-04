N, M = map(int,input().split())
check= []

SN = [1 for i in range(N)]
SM = [1 for i in range(M)]

for i in range(0,N):
    S = input()
    for j in range(0,M):
        if S[j] == 'X':
            SN[i] = 0 
            SM[j] = 0

sumN = sum(SN)
sumM = sum(SM)

output = sumN if sumN > sumM else sumM   

print(output)