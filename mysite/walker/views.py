from django.shortcuts import render
from datetime import datetime
from .models import Post

# walker/views.py.
def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html',{
        'post_list':post_list,
    })
def post_detail(request, pk):
    post = Post.objects.get(pk = pk)
    return render(request, 'post.html', {'post':post})