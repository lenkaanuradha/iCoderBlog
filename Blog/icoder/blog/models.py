from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    sno=models.IntegerField()
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=20)
    aboutauthor=models.CharField(max_length=500)
    views=models.IntegerField(default=0)
    content=models.TextField(max_length=1000)
    slug=models.CharField(max_length=30)
    timedate=models.DateField(blank=True)
    
    def __str__(self):
        return self.title
    
class BlogComment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment[0:10] + "..."+"by"+ self.user.username