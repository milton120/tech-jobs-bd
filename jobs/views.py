from django.shortcuts import render
from django.http import HttpResponse
from .models import JobPost
from django.views.generic.edit import CreateView
from django.views import generic


def index(request):
    return HttpResponse("Hello, world. You're at the job posts index.")


class JobPostCreate(CreateView):
    model = JobPost
    fields = '__all__'


class DetailView(generic.DetailView):
    model = JobPost
    template_name = 'jobs/detail.html'



