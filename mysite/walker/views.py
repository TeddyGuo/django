from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Post

# walker/views.py.
def home(request):
    post_list = Post.objects.all().order_by('-created_date')
    return render(request, 'home.html',{
        'post_list':post_list
    })
def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'post.html', {'post':post})