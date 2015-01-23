from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404


def post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {'post': post}
    return render(request, "blog/post.html", context)