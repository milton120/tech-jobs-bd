from django.conf.urls import url

from . import views
app_name = 'jobs'

urlpatterns = [
    url(r'^all/$', views.JobIndexView.as_view(), name='job-index'),
    url(r'^job-posts/add/$', views.JobPostCreateView.as_view(), name='job-post'),
    url(r'^(?P<pk>[0-9]+)/$', views.JobDetailView.as_view(), name='detail'),
    url(r'^company/registration/$', views.CompanyCreateView.as_view(), name='company-registration'),
    url(r'^company/(?P<pk>[0-9]+)/$', views.CompanyDetailView.as_view(), name='company-detail'),
    url(r'^company/all/$', views.CompanyIndexView.as_view(), name='company-index'),

]


