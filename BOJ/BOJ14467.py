N = int(input())

matrix = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    if matrix[i][0]