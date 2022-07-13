#주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.

#방법1
n = 'apple'
for i in n:
    if i == 'a':
        m =n.strip('a')
        print(m)

#방법2
n = 'apple'
result = ''
for i in n:
    if i != 'a':
        result = result + i
print(result)