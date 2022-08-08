K = int(input())

for test in range(1,K+1): #테스트 케이스 설정
    list_ = [] # 빈 리스트 생성
    N = list(map(int,input().split())) #입력값
    N.pop(0) #첫번째자리 삭제
    N.sort(reverse=True) #내림차순 설정
    for i in range(len(N)-1): #(len(N)-1)을 하지 않으면 범위가 벗어난다.)
        result = N[i] - N[i+1] #현재 점수와 다음칸의 점수를 뺀다.
        list_.append(result) #result에 저장
    print(f'Class {test}\nMax {max(N)}, Min {min(N)}, Largest gap {max(list_)}')
    #결과값 출력