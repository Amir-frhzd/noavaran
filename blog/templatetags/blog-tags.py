from django import template
from django.utils import timezone
from blog.models import Category,Post
register = template.Library()

@register.filter
def snippet(value,arg=20):
    return value[:arg] + ('...' if len(value) > arg else '')

@register.inclusion_tag('blog/blog-latest-post.html')
def latestposts():
    posts=Post.objects.filter(status=1,published_date__lte=timezone.now()).order_by('-published_date')[:3]
    
    return {'posts':posts}
