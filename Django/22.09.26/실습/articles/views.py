from django.shortcuts import render
import random

# Create your views here.

def index(request):
    return render(request, 'index.html')

def judge(request, number):

    context = {
        'num': number,
    }

    return render(request,'is-odd-even.html', context)

def calculate(request, A, B):


    result_add = A + B
    result_sub = A - B
    result_mul = A * B
    result_div = A // B

    context = {
        'add' : result_add,
        'sub' : result_sub,
        'mul' : result_mul,
        'div' : result_div,        
    }

    return render(request, 'calculate.html', context)


def life(request):
    return render(request, 'life-random.html')

def show(request):
    return render(request, 'life-random-show.html')

def lorem(request):
    return render(request, 'lorem-lipsum.html')

def loremshow(request):
    line_ = request.GET.get("line_cnt")
    word_ = request.GET.get("word_cnt")

    word = ["바나나", "사과", "딸기", "배", "파인애플"]
    list_ = []

    for i in range(int(line_)):
        M = [random.choice(word) for j in range(int(word_))]
        list_.append(M)
    
    context = {
        "list_" : list_,
    }
    return render(request, 'lorem-lipsum-show.html', context)





