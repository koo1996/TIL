N = int(input())
Y = list(map(int,input().split()))
Y.sort()
print(Y[0]*Y[-1])