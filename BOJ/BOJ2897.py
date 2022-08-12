R,C = map(int,input().split()) # R x C 행렬 생성
map_ = [list(input()) for _ in range(R)]

cnt0 = 0 # 차 부수지 않고 주차할 수 있는 공간의 개수 / 초기화
cnt1 = 0 # 차 1대 부수고 주차할 수 있는 공간의 개수 / 초기화
cnt2 = 0 # 차 2대 부수고 주차할 수 있는 공간의 개수 / 초기화
cnt3 = 0 # 차 3대 부수고 주차할 수 있는 공간의 개수 / 초기화
cnt4 = 0 # 차 4대 부수고 주차할 수 있는 공간의 개수 / 초기화

for i in range(R-1): # 차를 주차하기 위해서는 2 x 2 공간이 필요 / R, C에 1씩 빼준 위치까지는 검사하면 된다. 
    for j in range(C-1):
        check = [] #2 x 2 값들을 따로 리스트에 저장
        check.append(map_[i][j])
        check.append(map_[i][j+1])
        check.append(map_[i+1][j])
        check.append(map_[i+1][j+1])
        if check.count('#') == 0: # 만약에 '#'가 없으면
            if check.count('X') == 4: #check 리스트에 X의 갯수가 4개면 cnt4에 +1
                cnt4 += 1
            elif check.count('X') == 3: #check 리스트에 X의 갯수가 3개면 cnt3에 +1
                cnt3 += 1
            elif check.count('X') == 2: #check 리스트에 X의 갯수가 2개면 cnt2에 +1
                cnt2 += 1
            elif check.count('X') == 1: #check 리스트에 X의 갯수가 1개면 cnt1에 +1
                cnt1 += 1
            elif check.count('X') == 0: #check 리스트에 X의 갯수가 0개면 cnt0에 +1
                cnt0 += 1

print(cnt0,cnt1,cnt2,cnt3,cnt4,sep='\n') #결과값 출력

