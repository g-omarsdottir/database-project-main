from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here. "my_blog" from source code.
class PostList(generic.ListView):
    #queryset = Post.objects.all()
    queryset = Post.objects.filter(status=1)
template_name = "post_list.html"
