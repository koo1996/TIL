matrix = []
for _ in range(8): #8x8 행렬 생성
    matrix.append(input())
cnt = 0 # cnt 초기화
for i in range(8): 
    for j in range(8):
        if (i + j) % 2 == 0: # i + j 값을 2로 나눈 후에 나머지가 0이면 
            if matrix[i][j] == 'F': # 그 위치에 F가 있다면  cnt +1 한다
                cnt += 1
print(cnt) #cnt 출력한다.
