from django.forms import ModelForm
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import ListView, DetailView
from django.views.generic import UpdateView

from .models import Blog, Post


class BlogsView(ListView):
    template_name = 'blogs/blog_list.html'
    model = Blog


class PostsView(ListView):
    template_name = 'blogs/post_list.html'
    model = Post


class DetailedBlogView(DetailView):
    model = Blog
    template_name = 'blogs/detail_blog.html'


class DetailedPostView(DetailView):
    model = Post
    template_name = 'blogs/detail_post.html'


class EditBlogView(UpdateView):
    model = Blog
    template_name = 'blogs/create_blog.html'
    fields = ('title', 'description', 'categories',)

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user).all()

    def get_success_url(self):
        return reverse('blogs:blogs_list')


class CreateBlogView(CreateView):
    model = Blog
    template_name = 'blogs/create_blog.html'
    fields = ('title', 'description', 'categories',)

    def get_success_url(self):
        return reverse('blogs:blogs_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateBlogView, self).form_valid(form)


class CreatePostView(CreateView):
    model = Post
    template_name = 'blogs/create_post.html'
    fields = ('name', 'content',)

    _blog = None

    def dispatch(self, request, blog_id=None, *args, **kwargs):
        self._blog = get_object_or_404(Blog.objects.filter(author=self.request.user).all(), id=blog_id)
        return super(CreatePostView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('blogs:detail_blog', kwargs={'pk': self._blog.id})

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = self._blog
        return super(CreatePostView, self).form_valid(form)


class EditPostView(UpdateView):
    model = Post
    template_name = 'blogs/create_post.html'
    fields = ('name', 'content',)

    _blog = None

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).all()

    def dispatch(self, request, *args, **kwargs):
        self._blog = self.get_object().blog
        return super(EditPostView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('blogs:detail_blog', kwargs={'pk': self._blog.id})


class CreatePostInBlogForm(ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'content', 'blog',)

    def __init__(self, user=None, **kwargs):
        super(CreatePostInBlogForm, self).__init__(**kwargs)
        self.fields['blog'].queryset = Blog.objects.filter(author=user).all()


class CreatePostInBlog(CreateView):
    template_name = 'blogs/create_post.html'

    def get_form(self, form_class=None):
        return CreatePostInBlogForm(self.request.user)

    def get_success_url(self):
        return reverse('blogs:detail_blog', kwargs={'pk': self.object.blog.id})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePostInBlog, self).form_valid(form)
