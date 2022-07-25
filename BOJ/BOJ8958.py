# https://www.acmicpc.net/problem/8958

for test_1 in range(int(input())):
    cnt = 0
    res = 0
    for test_2 in (input()):
        if test_2 == 'O':
            cnt += 1
            res = res + cnt
        elif test_2 == 'X':
            cnt = 0
    print(res) 