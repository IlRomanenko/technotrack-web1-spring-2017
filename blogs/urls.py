"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import BlogsView, PostsView, DetailedBlogView, DetailedPostView, CreateBlogView, CreatePostView
from .views import EditBlogView, EditPostView

# ?P<blog_id>[0-9]+


urlpatterns = [
    url(r'^$', BlogsView.as_view(), name='blogs_list'),
    url(r'^blog/(?P<pk>\d+)/$', DetailedBlogView.as_view(), name='detail_blog'),

    url(r'^blog/(?P<pk>\d+)/edit', login_required(EditBlogView.as_view()), name='edit_blog'),
    url(r'^blog/create$', login_required(CreateBlogView.as_view()), name='create_blog'),

    url(r'^posts/$', PostsView.as_view(), name='posts_list'),
    url(r'^post/(?P<pk>\d+)/$', DetailedPostView.as_view(), name='detail_post'),

    url(r'^post/(?P<pk>\d+)/edit', login_required(EditPostView.as_view()), name='edit_post'),
    url(r'^post/create/(?P<blog_id>\d+)/$', CreatePostView.as_view(), name='create_post'),
]
