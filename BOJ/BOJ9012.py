for i in range(int(input())):
    stack = []
    N = input()
    for j in N: 
        if j == '(': #입력값에 (가 있다면
            stack.append(j) #stack에 저장
        elif j == ')': #)가 있다면
            if '(' in stack: #stack안에 (가 있으면
                stack.pop() #stack 오른쪽에 있는 (삭제
            else:
                print('NO') #stack안에 (가 없다면 NO 출력하고 break
                break
    else: #for문이 끝난 후에 stack이 비어있다면 YES출력, 아니면 NO 출력
        if not stack:
            print('YES')
        else:
            print('NO')