#문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
#find() index() 메서드 사용 금지

n = input()
count=0
for i in n:
    if i != 'a':
        count+=1
    elif i == 'a':
        print(count, end = ' ')
        count+=1

#word = 'banana'
#result = []
#for idx in range(len(word)):
#    if word[idx] == 'a':
#        result.append(idx) #리스트 추가
#print(result)