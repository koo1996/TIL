#월 : 계절 이름 / 계절 이름을 출력한다.
# 12, 1, 2 : winter
# 3, 4, 5 : spring
# 6, 7, 8 : summer
# 9, 10, 11 : fall

n = int(input())

if n//3 == 1:
    print('spring')
elif n//4.5 == 1:
    print('summer')
elif n//6 == 1:
    print('fall')
else:
    print('winter')
