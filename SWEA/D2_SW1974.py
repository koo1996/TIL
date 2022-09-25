T = int(input())

for test in range(1,T+1):
    matrix = []
    Small_box = []
    for i in range(9):
        N = list(map(int,input().split()))
        matrix.append(N)
    
    for j in range(3):
        for k in range(3):
            Small_box.append(matrix[j][k])
