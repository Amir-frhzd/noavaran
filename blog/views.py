from django.shortcuts import render,get_object_or_404
from .models import Post,Category
# Create your views here.
def blog_view(request,slug=None):
    posts=Post.objects.filter(status=1)
    if slug:
        posts=posts.filter(category__slug=slug)
    categories=Category.objects.all()
    context={'posts':posts,'categories':categories}
    return render(request,'blog/blog.html',context)

def single_view(request,pid):
    posts=get_object_or_404(Post,pk=pid,status=1)
    context={'post':posts}
    return render(request,'blog/blog-single.html',context)
