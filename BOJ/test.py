# history = list(map(str,input().split(',')))
# option = list(map(str,input().split(',')))
# keyword = input()
# answer = []
# if option[0] == "W" and option[1] == "T":
#     for i in history:
#         if keyword in i:
#             answer.append(i)
# print(answer)

a = ["83.12","25.44","56.39","12.67","11.11","66.55"]

sum_score = 0
cnt = 0
for i in a:
    sum_score += float(i)
    cnt += 1

sum_score = round(sum_score,2)
print(sum_score)       
answer = sum_score / cnt
answer = round(answer,4)
print(answer)