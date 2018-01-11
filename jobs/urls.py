from django.conf.urls import url

from . import views
from .views import JobPostCreate
app_name = 'jobs'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^job-posts/add/$', JobPostCreate.as_view(), name='job-post'),

]


