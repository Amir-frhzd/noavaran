from django.urls import path,re_path
from .views import *
app_name='blog'
urlpatterns = [
    path('',blog_view,name='blog'),
    #path('category/<slug:category_slug>',blog_view,name='category'),
    re_path(r'^category/(?P<slug>[-\w]+)/',blog_view,name='category'),
    path('author/<str:str>',blog_view,name='author'),
    path('<int:pid>',single_view,name='single'),
    path('search/',search_view,name='search')
    

]
