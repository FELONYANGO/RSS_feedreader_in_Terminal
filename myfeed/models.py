from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
#custorm manager to retrieve all the post with publisshed row
class PublishedManager(models.Manager): 
    def get_queryset(self) :
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','draft'),
        ('published','published')
    )

    title = models.CharField(max_length=250)
    slug=models.CharField(max_length=250,unique_for_date='publish')
    author=models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    body =models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    objects= models.Manager()
    published=PublishedManager()

    class Meta:
       ordering = ("-publish",)

    def __self__(self):
        return self.title


        

