#a부터 입력한 문자까지 순서대로 공백을 두고 한 줄로 출력한다.

n = ord(input())
count = ord('a')

while count <= n:
    count+=1
    print(chr(count-1), end=' ')