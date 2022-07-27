def solution(absolutes, signs): #absolutes[] : 정수저장 signs[] : true, false 저장
    for test in range(len(absolutes)): #absolutes길이만큼 반복
        if signs[test] == False: #signs[]에 False가 있다면 absolutes[] 같은 위치에 있는 정수에 -를 붙인다.
            absolutes[test] = -absolutes[test]
    answer = sum(absolutes) #absolutes[] 값들을 더한다.

    return answer