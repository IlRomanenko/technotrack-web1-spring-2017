from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import ListView

from blogs.models import Post
from comments.models import Comment


class CommentsView(ListView):
    template_name = 'comments/comment_list.html'
    model = Comment

    pass


class AddCommentView(CreateView):
    model = Comment
    fields = ('content',)
    template_name = 'comments/add_comment.html'

    _post = None

    def get_success_url(self):
        return reverse('blogs:detail_post', kwargs={"pk": self._post.id})

    def dispatch(self, request, post_id=None, *args, **kwargs):
        self._post = get_object_or_404(Post.objects.all(), id=post_id)
        return super(AddCommentView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self._post
        return super(AddCommentView, self).form_valid(form)

    pass
