from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blog' #Anything we can keep, need to inclode in template

urlpatterns = [
    path('', views.all_blogs, name="all_blogs"),
    path('<int:blog_id>/', views.blogDetail, name="detail"),
]