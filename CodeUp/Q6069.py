#평가 내용 / 문자에 따라 다른 내용이 출력된다.
#A : best!!!
#B : good!!
#C : run!
#D : slowly~
#나머지 문자들 : what?

n = input()
if n == 'A':
    print('best!!!')
elif n == 'B':
    print('good!!')
elif n == 'C':
    print('run!')
elif n == 'D':
    print('slowly~')
else:
    print('what?')