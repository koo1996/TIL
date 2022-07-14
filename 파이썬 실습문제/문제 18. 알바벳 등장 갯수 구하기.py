#문자열 word가 주어질 때, Dictionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.

#alphabet = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0
#, 'g' : 0, 'h' : 0, 'i' : 0, 'j' : 0, 'k' : 0, 'l' : 0
#, 'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0
#,'s' : 0, 't' : 0,'u' : 0, 'v' : 0, 'w' : 0,'x' : 0,'y' : 0, 'z' : 0}

#n = input()

#for x in n:
#    alphabet[x]+= 1
#for y in alphabet.values():
#    print(y)

word = 'banana'

result = {}
for char in word:
    if not char in result:
        result[char] = 0
    else:
        result[char] = result[char] + 1
print(result)

#3
result = {}
for char in word:
    #result['a'] 없으면 KeyError
    #result.get('a') 기본값이 None
    #result.get('a', 0) 기본값이 0
    result[char] = result.get(char, 0)+1
print(result)

for key in result:
    print(key, result[key])