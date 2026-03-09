from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        Post.objects.create(author=request.user, content=content)
        return redirect('home')
    return render(request, 'create_post.html')

@login_required
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('home')