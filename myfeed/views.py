from django.shortcuts import render,get_object_or_404
from .models import Post

def post_list(request):
    post=Post.published.all()

    return render(request,'myfeed/post/list.html',{'post':post})

def post_retrieve(request,year,month,day,posts):
    posts = get_object_or_404(Post,slug=Post, 
                    status='published',publish_year=year,
                    publish_month=month)

    return render(request,myfeed/post/retrieve.html,{'posts':posts})
