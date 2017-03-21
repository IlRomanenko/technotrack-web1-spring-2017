from django.http import HttpResponse
from django.views.generic import TemplateView

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
    pass
