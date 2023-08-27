from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from data_details.models import User,Blog,Commands

# Create your views here.
@api_view(['POST'])
def user(request):
    name=request.POST.get('name',None)
    if name is None:
        context={
            'message':'name is missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            new_record=User.objects.create(
                name=name
            )
            new_record.save()
            context={
                'message':'successfully added the user',
                'data':{
                    'user_id':new_record.id,
                    'name':new_record.name
                }
            }
            return Response(context,status=status.HTTP_200_OK)
        except ValueError:
            context={
                'message':'invalid name'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_blog(request):
    title=request.POST.get('title',None)
    if title is None:
        context={
            'message':'title is missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            new_record=Blog.objects.create(
                title=title
            )
            new_record.save()
            context={
                'message':'successfully added the title',
                'data':{
                'blog_id':new_record.id,
                'title':new_record.title,
            }
        }
            return Response(context,status=status.HTTP_200_OK)
        except ValueError:
            context={
                'message':'invalid...'
            }
            return Response(context,status=status.HTTP_BAD_REQUEST)

api_view(['GET'])
def list_blog(request):
    all_blogs=Blog.objects.all()
    data=[]
    for blog in all_blogs:
        temp={
            'blog_id':blog.id,
            'blog_name':blog.name
        }
        data.append(temp)
        context={
            'data':data
        }
        return Response(context,status=status.HTTP_200-OK)

@api_view(['PATCH'])
def update_blog(request):
    blog_id=request.POST.get('blog-id',None)
    new_blog=request.POST.get('new_blog',None)
    if blog_id is None:
        context={
            'message':'blog_id is miising'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            get_blog=Blog.objects.get(id=blog_id)
            get_blog.name=new_blog if new_blog is None else get_blog.name
            get_blog.save()
            context={
                'blog_id':get_blog.id,
                'blog_name':get_blog.name
            }
            return Response(context,status=status.HTTP_200_OK)
        except Blog.DoesNotExist:
            context={
                'message':'invalid blog_id'
            }
            return Response(context,status=status.HTTP_400_BAD-REQUEST)
        except valueError:
            context={
                'message':'invalisd_id'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete_blog(request):
    blog_id=request.POST.get('blog_id',None)
    if blog_id is None:
        context={
            'message':'blog-id is missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            get_blog=Blog.objects.get(id=blog_id)
            get_blog.delete()
            context={
                'message':'successfully deleted'
            }
            return Response(context,status=status.HTTP_200_OK)
        except ValueError:
            context={
                'message':'invalid...'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def commands(request):
    user=request.POST.get('user',None)
    if user is None:
        context={
            'message':'user is missing..'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            new_record=Commands.objects.create(
                user=user
            )
            new_record.save()
            context={
                'message':'successfully added command',
                'data':{
                    'blog_id':new_record.id,
                    'user':new_record.user
                }
            }
            return Response(context,status=status.HTTP_200_OK)
        except ValueError:
            context={
                'message':'invalid....'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)






