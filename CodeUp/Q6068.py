#평가 결과를 출력한다.
#점수 범위 : 평가
#90 ~ 100 : A
#70 ~   89 : B
#40 ~   69 : C
#0 ~   39 : D 로 평가되어야 한다.

n = int(input())

if n <= 40:
    print('D')
elif n <= 69:
    print('C')
elif n <= 89:
    print('B')
elif n <= 100:
    print('A')
else:
    print('Error')
