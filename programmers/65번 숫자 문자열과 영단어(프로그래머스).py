def solution(s):
    answer = s
    dic = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    #딕셔너리 생성
    for key,value in dic.items():
        answer = answer.replace(key, value)
    #answer에 key값을 value값으로 바꾼다.
    return int(answer) #정수형으로 변경
