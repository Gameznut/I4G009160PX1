from django.shortcuts import render
from django.urls import reverse_lazy, __all__

import blog
from blog.models import Post


class PostListView:
    model = Post


class PostCreateView:
    model = Post
    fields = __all__
    success_url = reverse_lazy(blog)


class PostDetailView:
    model = Post


class PostUpdateView:
    model = Post
    fields = __all__
    success_url = reverse_lazy(blog)


class PostDeleteView:
    model = Post
    fields = __all__
    success_url = reverse_lazy(blog)
