from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

# Create your models here.


class Company(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField("about company")
    location = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)
    total_job_posted = models.IntegerField(default=0)
    company_website = models.URLField(default='')


class Category(models.Model):
    job_category = models.CharField(max_length=50)

    def __str__(self):
        return self.job_category


class JobPost(models.Model):

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    job_title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    vacancy = models.IntegerField()
    job_nature = models.CharField(max_length=50)
    job_description = models.TextField()
    job_requirement = models.TextField()
    educational_requirement = models.CharField(max_length=200)
    experience_needed = models.CharField(max_length=50)
    age_range = models.CharField(max_length=50)
    job_location = models.CharField(max_length=200)
    salary_range = models.CharField(max_length=50)
    apply_instruction = models.TextField()
    job_posted_date = models.DateField(auto_now_add=True)
    job_deadline = models.DateField()

    def __str__(self):
        return self.job_title

    def slug(self):
        return slugify(self.job_title)


@receiver(post_save, sender=User)
def create_user_company(sender, instance, created, **kwargs):
    if created:
        Company.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_company(sender, instance, **kwargs):
    instance.company.save()



