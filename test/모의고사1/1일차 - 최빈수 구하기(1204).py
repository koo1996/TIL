
for test in range(int(input())):

    N = int(input())
    list_num = [] #빈 리스트 생성
    for i in range(0,101): #0부터100까지 반복
        list_num.append(0) #
    numbers = list(map(int,input().split())) 
    for i in range(len(numbers)): #number리스트에 있는 정수들이 있으면 
        if numbers[i] in numbers: #list_num에 1씩 추가
            X = numbers[i]
            list_num[X]+=1
    for y in range(100,-1,-1): #100부터 1씩 감소하면서 max(list_num)랑 같으면 인덱스 출력
        if max(list_num) == list_num[y]:
            print('#{} {}'.format(N,y))
            break
