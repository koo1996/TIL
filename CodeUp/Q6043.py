#f1을 f2로 나눈 결과를 소숫점 이하 넷째 자리에서 반올림하여 소숫점 세 번째 자리까지 출력한다.
a,b = input().split()
c = float(a) / float(b)
print(format(c,".3f"))