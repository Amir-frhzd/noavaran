from django.contrib import admin
from .models import Post,Category,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "published_date"
    empty_value_display = "-empty-"
    list_display = ['id','author','title','counted_view','status','created_date',]
    list_filter = ['status']
    #ordering=['-created_date']
    search_fields = ["title"]
class CategoryAdmin(admin.ModelAdmin):
    list_display =['name','slug']
    prepopulated_fields={'slug':('name',)}
class CommentAdmin(admin.ModelAdmin):
    list_display =['name','email','message','created_date','update_date',]
admin.site.register(Comment,CommentAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)