from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from data_details.models import User,Blog,Comments

# Create your views here.
@api_view(['POST'])
def add_user(request):
    user_name=request.POST.get('user_name',None)
    phone_number=request.POST.get('phone_number',None)
    location=request.POST.get('location',None)
    if user_name is None or phone_number is None or location is None:
        context={
            'message':'user_name/phone_number/location is missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            new_record=User.objects.create(
                user_name=user_name,
                phone_number=phone_number,
                location=location
            )
            new_record.save()
            context={
                'message':'successfully added the user',
                'data':{
                    'user_id':new_record.id,
                    'user_name':new_record.user_name,
                    'phone_number':new_record.phone_number,
                    'location':new_record.location
                }
            }
            return Response(context,status=status.HTTP_200_OK)
        except ValueError:
            context={
                'message':'invalid name'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_user(request):
    all_users=User.objects.all()
    data=[]
    for user in all_users:
        temp={
            'user_id':user.id,
            'user_name':user.user_name,
            'phone_number':user.phone_number,
            'location':user.location
        }
        data.append(temp)
        context={
            'data':data
        }
        return Response(context,status=status.HTTP_200_OK)
@api_view(['PATCH'])
def update_user(request):
    user_id=request.POST.get('user_id',None)
    new_user_name=request.POST.get('new_user_name',None)
    new_phone_number=request.POST.get('new_phone_number',None)
    new_location=request.POST.get('new_location',None)
    if user_id is None or new_user_name is None or new_phone_number is None or new_location is None:
        context={
            'message':'user_id/new_user_name/new_phone_number/new_location is missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            get_user=User.objects.get(id=user_id)
            get_user.name=new_user if new_user is None else get_user.name
            get_user.phone_number=new_phone_number if new_phone_number is None else get_user.phone_number
            get_user.location=new_location if new_location is None else get_user.location
            get_user.save()
            context={
                'message':'user updated successfully',
                'user_id':get_user.id,
                'user_name':get_user.name,
                'user_phone-number':get_user.phone_number,
                'user_location':get_user.location
            }
            return Response(context,status=status.HTTP_200_OK)
        except User.DoesNotExist:
            context={
                'message':'invalid user_id'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            context={
                'message':'invalid user_id'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request):
    user_id=request.POST.get('user_id',None)
    if user_id is None:
        context={
            'message':'user id missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            user=User.objects.get(id=user_id)
            user.delete()
            context={
                'message':'successfully deleted'
            }
            return Response(context,status=status.HTTP_200_OK)
        except ValueError:
            context={
                'message':'invalid user id'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            context={
                'message':'invalid user id'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_blog(request):
    user_id=request.POST.get('user_id',None)
    title=request.POST.get('title',None)
    description=request.POST.get('description',None)
    if user_id is None or title is None or description is None :
        context={
            'message':'user_id/title/description is missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            new_record=Blog.objects.create(
                user_id=user_id,
                title=title,
                description=description
            )
            new_record.save()
            context={
                'message':'successfully created new record',
                'data':{
                'user_id':new_record.user_id,
                'title':new_record.title,
                'description':new_record.description,
                'created_at':new_record.created_at,
                'updated_at':new_record.updated_at
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
            'user_id':blog.user_id,
            'title':blog.title,
            'description':blog.description,
            'created-at':blog.created_at,
            'updated_at':blog.updated_at
        }
        data.append(temp)
        context={
            'data':data
        }
        return Response(context,status=status.HTTP_200-OK)

@api_view(['PATCH'])
def update_blog(request):
    blog_id=request.POST.get('blog_id',None)
    new_title=request.POST.get('new_title',None)
    new_description=request.POST.get('new_description',None)
    if blog_id is None or new_title is None or new_description is None:
        context={
            'message':'blog_id/new_blog_title/new_blog_description is missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            get_blog=Blog.objects.get(id=blog_id)
            get_blog.name=new_blog if new_blog is None else get_blog.name
            get_blog.description=new_description if new_description is None else get_blog.description
            get_blog.title=new_title if new_title is None else get_blog.title
            get_blog.save()
            context={
                'message':'blog updated successfully',
                'blog_id':get_blog.id,
                'blog_name':get_blog.name,
                'blog_title':get_blog.title,
                'blog_description':get_blog.description
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
def add_comments(request):
    user_id=request.POST.get('user_id',None)
    blog_id=request.POST.get('blog_id',None)
    comments=request.POST.get('comments',None)
    if user_id is None or blog_id is None or comments is None:
        context={
            'message':'user_id/blog_id/comments is missing..'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            new_record=Comments.objects.create(
                user_id=user_id,
                blog_id=blog_id,
                comments=comments
            )
            new_record.save()
            context={
                'message':'successfully added comment',
                'data':{
                    'blog_id':new_record.id,
                    'comments':new_record.comments
                }
            }
            return Response(context,status=status.HTTP_200_OK)
        except ValueError:
            context={
                'message':'invalid comments...'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_comments(request):
    all_comments=Comments.objects.all()
    data=[]
    for comments in all_comments:
        temp={
            'blog_id':comments.id,
            'comments':comments.comments,
            'created_at':comments.created_at,
            'updated_at':comments.updated_at
        }
        data.append(temp)
        context={
            'data':data
        }
        return Response(context,status=status.HTTP_200_OK)
@api_view(['PATCH'])
def update_comments(request):
    comments_id=request.POST.get('comments_id',None)
    if comments_id is None:
        context={
            'message':'comments_id is missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            get_comments=Comments.objects.get(id=comments_id)
            get_comments.save()
            context={
                'message':'comments updated successfully'
            }
            return Response(context,status=status.HTTP_200-OK)
        except Comments.DoesNotExist:
            context={
                'message':'invalid comments_id'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            context={
                'message':'invalid comments_id'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_comments(request):
    comments_id=request.POST.get('comments_id',None)
    if comments_id is None:
        context={
            'message':'comment_id is missing'
        }
        return Response(context,status=status.HTTP_400-BAD_REQUEST)
    else:
        try:
            comments=Comments.objects.get(id=comments_id)
            comments.delete()
            context={
                'message':'comment deleted successfully'
            }
            return Response(context,status=status.HTTP_200_OK)
        except ValuseError:
            context={
                'message':'invalid comments_id'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
