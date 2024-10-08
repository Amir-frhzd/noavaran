from django.urls import path,re_path
from .views import *
from blog.feeds import LatestEntriesFeed
app_name='blog'
urlpatterns = [
    path('',blog_view,name='blog'),
    path('category/<str:slug>',blog_view,name='category'),
    #re_path(r'^category/(?P<slug>[-\w]+)/',blog_view,name='category'),
    path('tag/<str:tag_name>',blog_view,name='tag'),
    path('author/<str:str>',blog_view,name='author'),
    path('<int:pid>',single_view,name='single'),
    path('search/',search_view,name='search'),
    path("rss/feed/", LatestEntriesFeed()),
    

]
