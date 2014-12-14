from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {}
    context['posts'] = posts
    return render(request, "blog/post_list.html", context)