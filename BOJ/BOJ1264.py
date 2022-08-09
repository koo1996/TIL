list_ = ['a','e','i','o','u'] #모음을 리스트에 저장
while True:
    N = list(input().lower()) #입력값을 모두 소문자로 바꾸고 리스트에 저장
    if N[0] == '#': # '#' 이 있다면 break
        break
    cnt = 0
    for j in N: #N에 모음이 있다면 cnt 1씩 증가한다.
        if j in list_:
            cnt += 1    
    print(cnt)