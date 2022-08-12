N = int(input())
remove_ = ['a','e','i','o','u'] #삭제할 목록

for test in range(1,N+1): #테스트케이스 설정
    N = list(input()) #입력값을 리스트에 저장
    result_ = [] #결과값 저장 리스트 설정, 리스트 초기화
    for i in range(len(N)): #입력값 길이만큼 반복
        if N[i] not in remove_: #삭제할 목록에 포함되지 않으면 result_ 리스트에 저장
            result_.append(N[i])
    print(f'#{test} ',*result_,sep='') #결과값 출력