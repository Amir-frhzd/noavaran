from django.shortcuts import render,get_object_or_404
from .models import Post,Category
from taggit.models import Tag
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.utils import timezone
# Create your views here.
def blog_view(request,slug=None,str=None,tag_name=None):
    posts=Post.objects.filter(status=1,published_date__lte=timezone.now())
    if slug:
        posts=posts.filter(category__slug=slug)
    if str:
        posts=posts.filter(author__first_name=str)
    if tag_name:
        posts=posts.filter(tags__name__in=[tag_name])
    try:
        posts=Paginator(posts,2)
        page_number=request.GET.get('page')
        posts= posts.get_page(page_number)
    except PageNotAnInteger:
        posts=posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    categories=Category.objects.all()
    tags=Tag.objects.all()
    context={'posts':posts,'categories':categories,'tags':tags}
    return render(request,'blog/blog.html',context)

def single_view(request,pid):
    posts=get_object_or_404(Post,pk=pid,status=1,published_date__lte=timezone.now())
    if posts:
        posts.counted_view += 1
        posts.save()
    tags =posts.tags.all()
    categories=posts.category.all()
    context={'post':posts,'tags':tags,'categories':categories}
    return render(request,'blog/blog-single.html',context)
def search_view(request):
    posts=Post.objects.filter(status=1)
    if request.method == 'GET' :
        #print(request.GET.get('s'))
        if s :=request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context ={'posts':posts}
    return render(request,'blog/blog.html',context)