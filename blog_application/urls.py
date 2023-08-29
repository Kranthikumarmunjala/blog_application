"""blog_application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from data_details.views import add_user,list_user,update_user,delete_user,add_blog,list_blog,update_blog,delete_blog,add_comments,list_comments,update_comments,delete_comments

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_user/', add_user,name='add_user' ),
    path('list_user/',list_user,name='list_user'),
    path('update_user/',update_user,name='update_user'),
    path('delete_user/',delete_user,name='delete_user'),
    path('add_blog/',add_blog,name='add_blog'),
    path('list_blog/',list_blog,name='list_blog'),
    path('update_blog/',update_blog,name='update_blog'),
    path('delete_blog/',delete_blog,name='delete_blog'),
    path('add_comments/',add_comments,name='add_comments'),
    path('list_comments/',list_comments,name='list_comments'),
    #path('update_comments/',update_comments,name='update_comments'),
    path('delete_comments/',delete_comments,name='delete_comments')
]
