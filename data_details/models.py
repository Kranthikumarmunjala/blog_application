from django.db import models

# Create your models here.
class User(models.Model):
    user_name=models.CharField(max_length=255)
    phone_number=models.BigIntegerField()
    location=models.CharField(max_length=255)
    def __str__(self):
        return str(self.user_name)
class Blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.title)

class Comments(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    blog=models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True, blank=True)
    comment=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.blog)