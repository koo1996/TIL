from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    # 1. DB에서 모든 글을 불러온다.
    posts = Post.objects.all()

    context = {
        'posts' : posts,
    }

    # 2. template에 보내준다.
    return render(request, 'posts/index.html', context)

def new(request):
    return render(request, 'posts/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    Post.objects.create(title=title, content=content)
    
    context = {
        'title' : title,
        'content' : content,
    }

    return redirect('posts:index')

def delete(reqeust, pk):
    # pk에 해당하는 글 삭제
    Post.objects.get(id=pk).delete()

    return redirect('posts:index')