N = int(input())
number_ = list(map(int,input().split()))
Final_ = []
for i in range(len(number_)):
    New_score = (number_[i] / max(number_)) * 100
    Final_.append(New_score)

print(sum(Final_) / N)
