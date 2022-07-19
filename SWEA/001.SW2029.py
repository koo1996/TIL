

T = int(input())  
result=[] # 리스트 생성
for test_case in range(1,T+1):  #T번 반복
    a,b = input().split() 
    a=int(a)
    b=int(b)
    c = a // b  # 몫을 c에 저장
    d = a % b   # 나머지를 d에 저장
    result.append('#%d %d %d' %(test_case,c,d)) #리스트에 저장

print(*result, sep='\n') #줄바꿈해서 출력