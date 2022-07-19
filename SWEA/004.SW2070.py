T = int(input())
res=[] # 리스트 생성
for test_case in range(1,T+1): #T번 반복
    a,b = input().split()
    if int(a) < int(b): #크기비교
        res.append('#%d <' %test_case)  #< , > , = 리스트에 저장
    elif int(a) > int(b):
        res.append('#%d >' %test_case)
    else:
        res.append('#%d =' %test_case)

print(*res, sep='\n') #줄바꿈해서 출력
