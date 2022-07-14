#소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
#.upper(), .swapcase() 사용 금지

n= input()
for i in n:
    i=ord(i)
    I=i-32
    I=chr(I)
    print(I,end='')

#for char in word:
#    print(chr(ord(char)-32), end='')
