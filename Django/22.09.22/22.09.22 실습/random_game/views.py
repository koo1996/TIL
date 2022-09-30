from django.shortcuts import render
import random
# Create your views here.

def index(request):

    return render(request,"index.html")


def today_dinner(request):
    dinner_list = [
        {"name": "돈까스","src":"https://recipe1.ezmember.co.kr/cache/recipe/2019/01/12/b9343d314206275c1b6d0d0c4fcc2ce71.jpg"},
        {"name": "냉면", "src":"https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Dongmu_Bapsang_02.jpg/1200px-Dongmu_Bapsang_02.jpg"},
        {"name": "육개장","src":"https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Korean_soup-Yukgaejang-01.jpg/250px-Korean_soup-Yukgaejang-01.jpg"},
        {"name": "된장찌개","src":"https://upload.wikimedia.org/wikipedia/commons/a/a5/Doenjang_jjigae.jpg"},        
    ]   

    context = {
        "dinner" : random.choice(dinner_list)
    }

    return render(request, "today_dinner.html", context)

def lotto(request):
    
    today_lotto = [3, 11, 15, 29, 35, 44]
    lotto_list = []
    for _ in range(5):
        lotto = random.sample(range(1,45),6)
        lotto_list.append(lotto)

    context = {
        "lotto_list": lotto_list,
        "today_lotto": today_lotto,
    }
    return render(request, "lotto.html", context)