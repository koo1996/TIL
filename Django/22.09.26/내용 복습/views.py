from django.shortcuts import render
import random

# Create your views here.
def index(request):

    names = ['1','2','3','4','5','6','7']

    name = random.choice(names)
    context = {
        'name': name,
        'img': 'https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg', 
    }
    #메인 페이지를 보여준다.
    return render(request, 'index.html', context)

def welcome(request, name):
    # 사람들이 /welcome/본인이름 입력하면 환영 인사와 이름을 동시에 보여준다.
    context = {
        'name': name,
        'greetings': [
            '안녕하세요', 'hello', 'guten tag', 'bon jour'
        ],
        'images': [
            'https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg',
            'https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg',
            'https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg',
        ],

    }
    return render(request, 'welcome.html', context)

def index2(request):
    return render(request, 'index2.html')

def ping(request):
    return render(request, 'ping.html')

def pong(request):
    # name = request.GET.get('ball')
    # context = {
    #     'name' : name,
    # }
    return render(request, 'pong.html', {'name': request.GET.get('ball')})
