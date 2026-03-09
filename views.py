# app/views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Profile

@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        Post.objects.create(author=request.user, content=content)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return JsonResponse({'status': 'liked'})

@login_required
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    profile = request.user.profile
    if user_to_follow == request.user:
        return JsonResponse({'status': 'cannot_follow_self'})
    
    if user_to_follow in profile.followers.all():
        profile.followers.remove(user_to_follow)
    else:
        profile.followers.add(user_to_follow)
    return JsonResponse({'status': 'followed'})