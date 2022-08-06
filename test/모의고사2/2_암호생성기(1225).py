for test in range(10): #테스트 케이스 10개
    T = int(input())
    N = list(map(int,input().split()))
    i = 1
    while True: 
        if i > 5: #i가 5보다 커진다면 i = 1로 초기화
            i = 1
        else:            
            sum = N[0] - i #첫번째 자리의 숫자에 i씩 빼준다.        
            if sum <= 0: #sum값이 음수나 0이면 리스트 마지막자리에 0을 추가한다.
                N.append(0)
                N.pop(0) #첫번째 자리의 숫자를 삭제하고 break한다.
                break
            else: #sum값이 양수라면 리스트 마지막자리에 sum을 추가한다
                N.append(sum)
                N.pop(0) #첫번째자리의 숫자를 지운다.
                i += 1 #i를 1 증가시킨다.
    print(f'#{T}',*N) #결과값 출력