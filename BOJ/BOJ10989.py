import sys
n = int(sys.stdin.readline())
b = [0] * 10001
for i in range(n):
    b[int(sys.stdin.readline())] += 1
for i in range(10001):
    if b[i] != 0:
        for j in range(b[i]):
            print(i)

#input()으로 입력을 받으면 메모리초과
#sys를 사용해 입력을 받아주고, 배열을 생성