#입력된 16진수에 1~F까지 순서대로 곱한, 16진수 구구단을 줄을 바꿔 출력한다.
#계산 결과도 16진수로 출력해야 한다.

n = int(input(), 16)

for i in range(1,16):
    print("%X*%X=%X" %(n, i, n*i))
    