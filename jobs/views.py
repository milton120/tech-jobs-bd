from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from .models import JobPost, Company
from django.views.generic.edit import CreateView
from django.views import generic
from django.views import View
from .forms import CompanyRegistrationForm
from django.core.urlresolvers import reverse

from django.contrib.auth import get_user_model
CustomUser = get_user_model()


class JobIndexView(generic.ListView):
    template_name = 'jobs/job_index.html'
    context_object_name = 'all_jobs'  # replacing default 'object_list' name to 'all_jobs' for front end

    def get_queryset(self):
        return JobPost.objects.all()


class JobPostCreateView(CreateView):
    model = JobPost
    fields = '__all__'


class JobDetailView(generic.DetailView):
    model = JobPost
    template_name = 'jobs/detail.html'


class CompanyCreateView(View):
    form_class = CompanyRegistrationForm
    initial = {'key': 'value'}
    template_name = 'jobs/company_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password2']
            user = CustomUser.objects.create_user(email, password)
            print("custom user is created successfully.")
            company = Company()
            company.email = user
            company.name = form.cleaned_data['name']
            company.about = form.cleaned_data['about']
            company.location = form.cleaned_data['location']
            company.company_website = form.cleaned_data['company_website']
            company.save()

            return redirect(company)  # redirect will call get_absolute_url method of Company model


class CompanyIndexView(generic.ListView):
    template_name = 'jobs/company_index.html'
    context_object_name = 'all_companies'  # replacing object_list with all_companies
    # paginate_by = 10

    def get_queryset(self):
        return Company.objects.all()


class CompanyDetailView(generic.DetailView):
    model = Company
    template_name = 'jobs/company_detail.html'




