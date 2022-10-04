# URL 설정을  app 단위로!
from django.urls import path
from . import views
app_name = 'articles'

urlpatterns = [
    # http://localhost:8000/
    path('', views.index, name='index'),
    # path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]