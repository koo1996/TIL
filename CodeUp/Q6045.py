#합과 평균을 공백을 두고 출력한다.
#평균은 소숫점 이하 셋째 자리에서 반올림하여 둘째 자리까지 출력한다.

a,b,c = input().split()

sum = int(a) + int(b) + int(c)
ave = float(sum) / 3 
print(sum,format(ave,".2f"))