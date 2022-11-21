import sys
n = int(input())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
for i in sorted(l):
    sys.stdout.write(str(i)+'\n')

## sys.stdout 출력 버퍼, 출력 버퍼가 지정되어 있지 않으면 터미널 출력  (표준 출력)