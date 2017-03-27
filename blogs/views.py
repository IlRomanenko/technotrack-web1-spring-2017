from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import ListView, DetailView
from django.views.generic import UpdateView

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
    template_name = 'blogs/detail_blog.html'

    pass


class DetailedPostView(DetailView):
    model = Post
    template_name = 'blogs/detail_post.html'

    pass


class EditBlogView(UpdateView):
    model = Blog
    template_name = 'blogs/create_blog.html'
    fields = ('title', 'description', 'categories',)

    def get_success_url(self):
        return reverse('blogs:blogs_list')

    pass


class CreateBlogView(CreateView):
    model = Blog
    template_name = 'blogs/create_blog.html'
    fields = ('title', 'description', 'categories',)

    def get_success_url(self):
        return reverse('blogs:blogs_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateBlogView, self).form_valid(form)

    pass


class CreatePostView(CreateView):
    model = Post
    template_name = 'blogs/create_post.html'
    fields = ('name', 'content',)

    _blog = None

    def dispatch(self, request, blog_id=None, *args, **kwargs):
        self._blog = get_object_or_404(Blog.objects.all(), id=blog_id)
        return super(CreatePostView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('blogs:detail_blog', kwargs={'pk': self._blog.id})

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = self._blog
        return super(CreatePostView, self).form_valid(form)

    pass


class EditPostView(UpdateView):
    model = Post
    template_name = 'blogs/create_post.html'
    fields = ('name', 'content', )

    _blog = None

    def dispatch(self, request, *args, **kwargs):
        self._blog = self.get_object().blog
        return super(EditPostView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('blogs:detail_blog', kwargs={'pk': self._blog.id})

    pass
