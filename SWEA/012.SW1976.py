N = int(input())

for test in range(N): #N번 반복
    result=[] # 빈 리스트 생성
    a,b,c,d = map(int,input().split())
    hour = a + c #시간끼리 더하기
    if hour > 12: #12 넘으면 빼기
        hour = hour - 12
    result.append(hour) #리스트에 추가
    
    minute = b + d #분끼리 더하기
    if minute > 60: #60 넘으면 빼기
        minute = minute - 60 #시간에 +1
        hour+=1
    result.append(minute)
    print('#{} {} {}'.format(test+1,hour,minute) )