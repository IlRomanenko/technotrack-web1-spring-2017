from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import UserCreationForm
from django.forms import FileField
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView, CreateView

from blogs.models import Blog, Post
from comments.models import Comment


def test(request):
    return HttpResponse("test")


class IndexView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = {'blogs_total': Blog.objects.count(), "posts_total": Post.objects.count(),
                   "comments_total": Comment.objects.count()}
        return context


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'avatar')
        field_classes = {'avatar': FileField}


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'core/register.html'

    def get_success_url(self):
        login(self.request, self.object)
        return reverse('core:mainpage')

    def form_valid(self, form):
        return super(RegisterView, self).form_valid(form)
