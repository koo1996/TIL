matrix = [[0 for i in range(101)] for j in range(101)]
# 100 x 100 행렬생성
for _ in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1,x2): # 가로 x1~x2  세로 y1~y2 해당되는 자리에 0을 1로 바꾼다.
        for j in range(y1,y2):
            matrix[i][j] = 1

answer = 0
for k in matrix: #matrix에 모든 수를 더해준다.
    answer += sum(k)
print(answer)