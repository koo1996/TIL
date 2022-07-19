#방법1
N = input()
result=0
for i in N:
    result+=int(i)
print(result)

#방법2

number = 123
result = 0
while number:
    result += number % 10
    number //= 10

print(result)

#방법3
#divmod(x, y)는 x를 y로 나누고, 결과를 tuple로 반환
#(몫 / 나머지)
number, remainder = divmod(number, 10)
result += remainder

print(result)