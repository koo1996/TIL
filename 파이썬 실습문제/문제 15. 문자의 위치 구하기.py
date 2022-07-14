#문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
#a가 없는 경우에는 -1을 출력해주세요.
#find() index() 메서드 사용 금지

n = input()
count=0

for i in n:
    if i != 'a':
        count+=1   
    elif i == 'a':
        break
if count == len(n):
    print('-1')
else:
    print(count)

#for idx in range(len(word)):
#    if word[idx] == 'a':
#        print(idx)
#        break
#else:
#    print(-1)