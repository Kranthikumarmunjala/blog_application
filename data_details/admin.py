from django.contrib import admin
from .models import User,Blog,Commands
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['id','name','phone_number','location']

class BlogAdmin(admin.ModelAdmin):
    list_display=['id','title','description','created_at','updated_at']
    list_filter=['title']
    search_fields=['id']

class CommandsAdmin(admin.ModelAdmin):
    list_display=['id','user','blog','created_at','updated_at']
    list_filter=['user']
    search_fields=['id']

admin.site.register(User,UserAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Commands,CommandsAdmin)