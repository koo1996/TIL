def magic(num):
    count = 0
    for i in range(num+1, 2*num):
        count += 1
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                count -= 1
                break
    return count

while True:
    n = int(input())
    if n == 0:
        break
    elif n == 1:
        print(1)
    else:
        print(magic(n))