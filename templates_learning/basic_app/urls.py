from django.conf.urls import url
from basic_app import views
from django.contrib import admin



app_name = 'basic_app'

urlpatterns = [
    url(r'^admin', admin.site.urls),

    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other')
]
