#첫 번째 줄에 합
#두 번째 줄에 차,
#세 번째 줄에 곱,
#네 번째 줄에 몫,
#다섯 번째 줄에 나머지,
#여섯 번째 줄에 나눈 값을 순서대로 출력한다.
#(실수, 소수점 이하 둘째 자리까지의 정확도로 출력)

a,b = input().split()
sum1 = int(a) + int(b)
sum2 = int(a) - int(b)
sum3 = int(a) * int(b)
sum4 = int(a) // int(b)
sum5 = int(a) % int(b)
sum6 = float(a) / float(b)

print(sum1)
print(sum2)
print(sum3)
print(sum4)
print(sum5)
print(format(sum6,".2f"))