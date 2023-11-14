from django.shortcuts import render
from .models import Post

def postapp(requst):
    posts = Post.objects.all
    print(posts)