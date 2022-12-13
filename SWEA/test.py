numbers = list(map(int,input().split()))
numbers.sort()

total = 0
count = 0

for i in range(1, len(numbers) - 1):
    total = total + numbers[i]
    count = count + 1
    print(total // count)
