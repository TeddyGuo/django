from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from .models import Post
from .forms import PostForm
from django.utils import timezone

# walker/views.py.
def home(request):
    post_list = Post.objects.all().order_by('-created_date')
    return render(request, 'home.html',{
        'post_list':post_list
    })
def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'post.html', {'post':post})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})
