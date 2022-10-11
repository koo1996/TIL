from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.

def index(request):
    
    # 게시글을 가져와서
    articles = Article.objects.order_by('-pk')
    # template 전달
    context = {
        'articles' : articles
    }
    # 페이지를 render...
    return render(request,'articles/index.html', context)
    
# def new(request):
#     article_form = ArticleForm()
#     context = {
#         'article_form': article_form
#     }
#     return render(request, 'articles/new.html', context=context)

def create(request):
    if request.method == 'POST':

        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/new.html', context=context)    
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # Article.objects.create(title=title, content=content)

def detail(request, pk):
    # 특정 글을 가져온다.
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        # POST : input 값 가져와서 검증하고, DB에 저장
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            # 유효성 검사 통과하면 상세보기 페이지로 전환
            article_form.save()
            return redirect('articles:detail', article.pk)
        # 유효성 검사 통과하지 않으면 -> context 부터해서 오류메시지 담긴 article_form
    else:    
        # GET : Form을 제공    
        article_form = ArticleForm(instance=article)
    context = {
        'article_form' : article_form
    }
    return render(request, 'articles/update.html', context)
