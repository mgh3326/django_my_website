from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from blog.models import Post


class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')
