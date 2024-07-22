from django import template
from django.utils import timezone
from blog.models import Category,Post,Comment
from bs4 import BeautifulSoup
register = template.Library()

@register.filter
def snippet(value,arg=20):
    if not value:
        return ''
    soup=BeautifulSoup(value,'html.parser')
    txt=soup.get_text()
    return txt[:arg]+ (' ...' if len(value) > arg else '')
    #return value[:arg] + ('...' if len(value) > arg else '')

@register.inclusion_tag('blog/blog-latest-post.html')
def latestposts():
    posts=Post.objects.filter(status=1,published_date__lte=timezone.now()).order_by('-published_date')[:3]
    
    return {'posts':posts}
@register.simple_tag(name='comment_count')
def comment(pid):
    comment= Comment.objects.filter(post=pid,approved=True).count()
    return comment

@register.inclusion_tag('blog/new.html')
def detail_comment(pid):
    comments=Comment.objects.filter(post=pid,approved=True)
    c={'comments':comments}
    return c    
