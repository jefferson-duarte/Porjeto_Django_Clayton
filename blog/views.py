from django.shortcuts import render
from .models import Post


def home(request):
    posts = Post.objects.all().order_by('-data_publicacao')[:5]
    context = {
        'post': posts,
    }

    return render(request, 'blog/home.html', context)


def post_detail(request, post_id):
    posts = Post.objects.get(pk=post_id)
    context = {
        'post': posts,
    }

    return render(request, 'blog/post_details.html', context)


def blog(request):
    return render(request, 'blog/blog.html')
