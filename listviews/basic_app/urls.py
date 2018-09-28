from django.conf.urls import url
from . import views

app_name = 'basic_app'

urlpatterns = [
    # url(r'^$', views.IndexView.as_view()),
    url(r'^$', views.SchoolListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', views.SchoolDetailView.as_view(), name='detail')

]
