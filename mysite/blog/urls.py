from django.conf.urls import url
from django.contrib.auth.views import login
from . import views


urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^login/$', login, name='login'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^post/(?P<pk>\d+)$', views.DetailView.as_view(), name='post_detail'),
    url(r'^post/new/', views.CreateView.as_view(), name='post_new'),
    url(r'post/(?P<pk>\d+)/edit/$', views.UpdateView.as_view(), name="post_edit"),
    url(r'post/(?P<pk>\d+)/remove/$', views.DeleteView.as_view(), name="post_remove"),
    url(r'^drafts/$', views.DraftListView.as_view(), name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'comment/(?P<pk>\d+)/remove/$', views.comment_delete, name="comment_remove"),
    url(r'post/(?P<pk>\d+)/publish/$', views.post_publish, name="post_publish"),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),

    ]
