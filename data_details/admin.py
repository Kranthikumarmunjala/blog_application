from django.contrib import admin
from .models import User,Blog,Comments
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['id','user_name','phone_number','location']
    list_filter=['user_name']
    search_fields=['user_name']

class BlogAdmin(admin.ModelAdmin):
    list_display=['id','user','title','description','created_at','updated_at']
    list_filter=['title']
    search_fields=['id','user']

class CommentsAdmin(admin.ModelAdmin):
    list_display=['id','user','blog','comment','created_at','updated_at']
    list_filter=['comment']
    search_fields=['id','user']

admin.site.register(User,UserAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comments,CommentsAdmin)