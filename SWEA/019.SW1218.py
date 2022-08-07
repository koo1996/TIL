for test in range(1,11): #테스트 케이스 설정
    list_1 = [] #입력값 문자열 저장할 리스트 생성
    N = int(input()) 
    string_input = input() #입력값 문자열
    for i in range(N): #문자열을 list_1 리스트에 저장
        list_1.append(string_input[i])
    list_2 = [] #검사할 리스트 생성
    for j in range(N): #입력한 문자열 길이만큼 반복
    #')'이면 list_2 에 -1번 자리(맨 마지막자리)에 '('있다면 list_2 마지막자리 값을 삭제한다.
        if list_1[j] == ')':  
            if list_2[-1] == '(': 
                list_2.pop() 
            else:
                list_2.append(list_1[j]) #아닌 경우에는 list_2에 저장한다.
    #']'이면 list_2 에 -1번 자리(맨 마지막자리)에 '['있다면 list_2 마지막자리 값을 삭제한다.
        elif list_1[j] == ']':
            if list_2[-1] == '[':
                list_2.pop()
            else:
                list_2.append(list_1[j]) #아닌 경우에는 list_2에 저장한다.
    #'}'이면 list_2 에 -1번 자리(맨 마지막자리)에 '{'있다면 list_2 마지막자리 값을 삭제한다.
        elif list_1[j] == '}':
            if list_2[-1] == '{':
                list_2.pop()
            else:
                list_2.append(list_1[j]) #아닌 경우에는 list_2에 저장한다.
    #'>'이면 list_2 에 -1번 자리(맨 마지막자리)에 '<'있다면 list_2 마지막자리 값을 삭제한다.
        elif list_1[j] == '>':
            if list_2[-1] == '<':
                list_2.pop()
            else:
                list_2.append(list_1[j]) #아닌 경우에는 list_2에 저장한다.
        else:
            list_2.append(list_1[j]) 
    if len(list_2) == 0: #list_2 길이가 0이면 1출력, 아니면 0 출력.
        answer = 1
    else:
        answer = 0
    print(f'#{test}',answer)