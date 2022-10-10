from django.shortcuts import render
import random

# Create your views here.

def index(request):
    return render(request, 'index.html')

def life(request):
    return render(request,'life-ago.html')

def judge(request, id):
    if id % 2 == 0:
        result = '짝수'
    else:
        result = '홀수'
    
    context = {
        'result': result, 'id': id
    }

    return render(request,'judge.html', context)

def calculator(request, A, B):

    if B == 0:
        return render(request, 'error.html')

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

    return render(request, 'calculator.html', context)


