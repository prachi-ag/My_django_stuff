from django.conf.urls import url
from . import views
# this is the first commit
app_name = 'kreiva'
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^userinfo/$', views.UserPartiInfo.as_view()),
    url(r'^userinfo/(?P<pk>[a-zA-Z0-9_.-]+)/$', views.UserPartiInfo.as_view()),
]