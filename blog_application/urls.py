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
from data_details.views import user,add_blog,list_blog,update_blog,delete_blog,commands

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', user,name='user' ),
    path('add_blog/',add_blog,name='add_blog'),
    path('list_blog/',list_blog,name='list_blog'),
    path('update_blog/',update_blog,name='update_blog'),
    path('delete_blog/',delete_blog,name='delete_blog'),
    path('commands/',commands,name='commands')
]
