#대시(마이너스 기호)를 구분기호로 사용해서
#일-월-연도로 바꿔 출력한다.
a,b,c = input().split('.')
a = int(a)
b = int(b)
c = int(c)
print(c,b,a,sep='-')