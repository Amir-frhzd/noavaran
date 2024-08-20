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
from django.utils.encoding import uri_to_iri
# Create your views here.
def blog_view(request,slug=None,str=None,tag_name=None):
    posts=Post.objects.filter(status=1,published_date__lte=timezone.now())
    if slug:
        slug = uri_to_iri(slug)
        posts=posts.filter(category__slug=slug)
    if str:
        str = uri_to_iri(str)
        posts=posts.filter(author__first_name=str)
    if tag_name:
        tag_name = uri_to_iri(tag_name)
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
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'نظر شما با موفقیت ثبت شد',fail_silently=True)


    posts=get_object_or_404(Post,pk=pid,status=1,published_date__lte=timezone.now())
    all_post=Post.objects.filter(status=1,published_date__lte=timezone.now())
    next_post =all_post.filter(id__gt=pid).order_by('id').first()
    previous_post=all_post.filter(id__lt=pid).order_by('-id').first()
    posts.save()
    if posts:
        posts.counted_view += 1
        posts.save()
    if not posts.login_require :
        tags =posts.tags.all()
        categories=posts.category.all()
        form=CommentForm()
        context={'post':posts,'tags':tags,'categories':categories,'form':form,'next_post':next_post,'previous_post':previous_post}
        return render(request,'blog/blog-single.html',context)
    elif request.user.is_authenticated :
        tags =posts.tags.all()
        categories=posts.category.all()
        form=CommentForm()
        context={'post':posts,'tags':tags,'categories':categories,'form':form,'next_post':next_post,'previous_post':previous_post}
        return render(request,'blog/blog-single.html',context)
    else :
        login_url=reverse('accounts:login')
        return HttpResponseRedirect(f'{login_url}?next={request.path}')
def search_view(request):
    posts=Post.objects.filter(status=1)
    if request.method == 'GET' :
    
        if s :=request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context ={'posts':posts}
    return render(request,'blog/blog.html',context)