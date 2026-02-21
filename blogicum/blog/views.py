from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Category, Post
from blog.constants import PUB_DATE_LIMIT


def get_published_posts():
    return Post.objects.select_related('category', 'location').filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ).order_by('-pub_date')


def index(request):
    post_list = get_published_posts()[:PUB_DATE_LIMIT]
    return render(request, 'blog/index.html', {'post_list': post_list})


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug, is_published=True)
    posts = get_published_posts().filter(category=category)
    return render(request, 'blog/category.html', {
        'post_list': posts,
        'category': category
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    if (
        not post.is_published
        or post.pub_date > timezone.now()
        or not post.category.is_published
    ):
        raise Http404
    return render(request, 'blog/detail.html', {'post': post})
