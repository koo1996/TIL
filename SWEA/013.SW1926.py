for test in range(1,int(input())+1): #input번 반복
    result=[]
    if test % 3 != 0: #나누기3 했을때 나머지 0이면
        result.append(test)
    else:
        result.append('-')
    print(*result, end=' ')