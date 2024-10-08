from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)
    slug =models.SlugField(max_length=100, unique=True,blank=True,null=True,allow_unicode=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name,allow_unicode=True)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name
class Post(models.Model):
    img=models.ImageField(upload_to='blog/',default='blog/default.jpg')
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title=models.CharField(max_length=255)
    content=models.TextField()
    tags = TaggableManager()
    category=models.ManyToManyField(Category)
    counted_view=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    published_date=models.DateTimeField(null=True)
    login_require=models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid': self.id})

    class Meta:
        ordering=['-created_date']
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    message=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now_add=True)
    approved=models.BooleanField(default=False)