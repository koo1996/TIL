# Django CRUD

> Django : 파이썬 기반 웹 프레임워크

## 1. 가상환경 및 Django 설치

> 가상환경 : 프로젝트별 별도 패키치 관리

### 1. 가상환경 생성 및 실행

* 가상환경 폴더를 '.gitignore'로 설정을 해둔다.
```bash
$ python -m venv venv
$ source venv/Scripts/activate
```

### 2. Django 설치 및 기록

```
$ pip install django==3.2.13
$ pip freeze > requirement.txt
```

### 3. Django 프로젝트 생성

```bash
$ django-admin startproject pjt
$ cd pjt
```

### 4. Django 앱 생성

> Django : 주요 기능 단위의 App 구조, App 별로 MTV를 구조를 가지는 모습 + 'urls.py'

```bash
$ python manage.py startapp articles
```
### 5. 앱 등록
* 'setting.py' 파일의 'INSTALLED_APPS'에 추가
```python
INSTALLED_APPS = [
    'articles',
]
```
### 5. urls.py 설정

> app 단위의 URL 관리
```python
# pjt/urls.py
urlpatterns = [
    path('articles/',include('articles.urls')),
]
```

```python
# articles/urls.py
urlpatterns = [
    path('', views.index, name='index'),
]
```

* 활용 : articles:index => '/articles/'

* Template에서 활용 예시
```django
{% url 'articles:index %}
```
* view에서 활용 예시


### 5. index

> url을 등록하고, view 함수 생성, template 만든다.

## 3. CRUD

### 3. Model 정의 (DB 설계)

#### 1. 클래스 정의
```
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

#### 2. 마이크래이션 파일 생성

* app 폴더 내의 'migrate' 폴더에 생성된 파일 확인
```bash
$ python manage.py makemirgrations
$ python manage.py migrate
```

#### 3. DB 반영
```
$ python manage.py migrate
$ python manage.py showmigrations
```

## 4. CRUD 기능 구현

### 0. ModelForm 선언

> 선언된 모델에 따른 필드 구성 (1) Form 생성 (2) 유효성 검사

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title','content']
```

### 1. 게시글 생성

> 사용자에게 HTML Form 제공, 입력한 데이터를 처리

#### 1. html form 제공

> GET http://localhost:8000/articles/create/

##### (1) urls.py

##### (2) view.py

```python
article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/new.html', context=context)    
```

##### (3) articles/create.html

* HTML Form 태그 활용시 핵심
    * 어떤 필드를 구성할 것인지 ('name', 'value)
    
    * 어디로 보낼 것인지('action','method')

```django
<h1>글쓰기</h1>

<form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ article_form.as_p }}
    <input type="submit" value="글쓰기"> 
</form>
```

#### 2. 입력받은 데이터 처리

> POST http://localhost:8000/articles/create/

### 2. 게시글 목록

> DB에서 게시글을 가져왓, template에 전달

## 5. Django ModelForm
* DB 기반의 어플리케이션을 개발하다보면, HTML Form(UI)은 Django의 모델(DB)과 매우 밀접한 관계를 가지게 됨
    * 사용자로부터 값을 받아 DB에 저장하여 활용하기 때문에




* 게시판
    * 생성
        * HTML Form
        * DB 저장 과정
        * /articles/new
        * /articles/create
    * 조회
        * 글을 누르면 DB값 조회
        * /articles/detail
    * 삭제
        * 버튼을 누르면 DB값 삭제
        * /articles/delete
    * 수정
        * HTML Form + 기존 값
        * DB 저장 과정
        * /articles/edit
        * /articles/update