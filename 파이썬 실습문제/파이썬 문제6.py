#주어진 리스트 numbers에서 
#최댓값을 구하여 출력하시오.
#max() 함수 사용 금지

numbers = [0, 20, 100]
#numbers = [0, 20, 100, 50, -60, 50, 100] # 100
#numbers = [0, 1, 0] # 1
#numbers = [-10, -100, -30] # -10 
x = numbers[0]

for i in numbers:
    if i > x:
        x = i
print(x)
