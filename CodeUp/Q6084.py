#필요한 저장 공간을 MB 단위로 바꾸어 출력한다.
#단, 소수점 첫째 자리까지의 정확도로 출력하고 MB를 공백을 두고 출력한다.

a,b,c,d = map(int,input().split())
sum = a * b * c * d / 8 / 1024 / 1024
print(format(sum,".1f"), 'MB')