from django.views.generic import ListView, DetailView
from .models import Blog, Post


class BlogsView(ListView):
    template_name = 'blogs/blog_list.html'
    model = Blog

    pass


class PostsView(ListView):
    template_name = 'blogs/post_list.html'
    model = Post

    pass


class DetailedBlogView(DetailView):
    model = Blog
    template_name = 'blogs/detail_blog_view.html'
    pass


class DetailedPostView(DetailView):
    model = Post
    template_name = 'blogs/detail_post_view.html'
    pass
