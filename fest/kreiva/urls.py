from django.conf.urls import url
from . import views
app_name = 'kreiva'
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^userinfo/$', views.UserPartyInfo.as_view()),
    url(r'^userinfo/(?P<pk>[a-zA-Z0-9_.-]+)/$', views.UserPartyInfo.as_view()),
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
]