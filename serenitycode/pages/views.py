from django.shortcuts import render
from blog.models import Post
from .models import Project


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'pages/index.html', context)


def projects_view(request):
    projects = Project.objects.all()
    context = {'projects' : projects}
    return render(request, 'pages/projects.html', context)