T = int(input())
res=[] # 리스트 생성
for test_case in range(1,T+1): #T번 반복
    numbers = list(map(int,input().split())) #리스트에 정수들 저장
    sum_numbers = sum(numbers) #정수들 합
    result = sum_numbers / len(numbers) #정수들 평균
    res.append('#%d %d' %(test_case,round(result))) #리스트 저장
print(*res, sep='\n') #줄바꿈해서 출력
