from django.shortcuts import render,get_object_or_404
from .models import Post,Category,Comment
from taggit.models import Tag
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.utils import timezone
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.db import connection
# Create your views here.
def blog_view(request,slug=None,str=None,tag_name=None):
    posts=Post.objects.filter(status=1,published_date__lte=timezone.now())
    if slug:
        posts=posts.filter(category__slug=slug)
    if str:
        posts=posts.filter(author__first_name=str)
    if tag_name:
        posts=posts.filter(tags__name__in=[tag_name])
        print(posts.query,'fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
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
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'نظر شما با موفقیت ثبت شد',fail_silently=True)


    posts=get_object_or_404(Post,pk=pid,status=1,published_date__lte=timezone.now())
    if posts:
        posts.counted_view += 1
        posts.save()
    if not posts.login_require :
        tags =posts.tags.all()
        categories=posts.category.all()
        form=CommentForm()
        context={'post':posts,'tags':tags,'categories':categories,'form':form}
        return render(request,'blog/blog-single.html',context)
    elif request.user.is_authenticated :
        tags =posts.tags.all()
        categories=posts.category.all()
        form=CommentForm()
        context={'post':posts,'tags':tags,'categories':categories,'form':form}
        return render(request,'blog/blog-single.html',context)
    else :
        login_url=reverse('accounts:login')
        return HttpResponseRedirect(f'{login_url}?next={request.path}')
def search_view(request):
    posts=Post.objects.filter(status=1)
    if request.method == 'GET' :
        #print(request.GET.get('s'))
        if s :=request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context ={'posts':posts}
    return render(request,'blog/blog.html',context)