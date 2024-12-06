from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator


def post_list(request):
    post_list = Post.objects.all().order_by('created_at')
    posts_per_page = request.GET.get('posts_per_page', 3)
    paginator = Paginator(post_list, posts_per_page)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'post1.html', {'posts': posts, 'posts_per_page': posts_per_page})
