T= int(input())


for test in range(1,T+1): #테스트케이스 설정
    A_list = [] #시작 덱 저장리스트 생성 , 초기화
    B_list = [] #다른 덱 저장리스트 생성 , 초기화
    result = [] #결과값 저장리스트 생성 , 초기화
    N = int(input()) #카드갯수
    Card_Name = list(input().split()) #카드 입력
    
    for i in range(N): #카드갯수에서 2를 나눈 값이 i 보다 작으면 A덱에 저장, 아니면 B덱에 저장
        if i < (N/2):
            A_list.append(Card_Name[i])
        else: 
            B_list.append(Card_Name[i])

    X = len(A_list) # A덱에 길이
    Y = len(B_list) # B덱에 길이

    for j in range(min(X,Y)): #최솟값인 덱에 길이만큼 반복
        result.append(A_list[j]) #A덱과 B덱을 번갈아가면서 result 리스트에 저장
        result.append(B_list[j])
    
    if N % 2 == 0: #카드갯수가 짝수면 그대로 result를 출력한다.
        print(f'#{test}',*result)
    else: #카드갯수가 홀수면 result 마지막자리에 카드갯수를 2로 나눈 몫의 위치에 있는 A_list 값을 추가하고 출력한다.
        print(f'#{test}',*result,A_list[N // 2])