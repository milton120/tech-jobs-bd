from django.conf.urls import url
from . import views

app_name = 'custom_user'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
