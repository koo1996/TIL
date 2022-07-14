#문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
#모음 : a, e, i, o, u 
#count() 사용 금지

n = input()
count=0
for i in n:
    if (i == 'a' or i == 'e' or i == 'i' 
    or i == 'o' or i == 'u'):
        count+=1
    
print(count)

#count = 0
#for char in word:
#    if char in 'aeiou':
#        count += 1
#print(count)