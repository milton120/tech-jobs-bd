from django import forms
from .models import JobPost


class JobPostForm(forms.ModelForm):

    class Meta:
        model = JobPost
        fields = '__all__'


class CompanyRegistrationForm(forms.Form):

    email = forms.EmailField(label='email')
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password confirmation', widget=forms.PasswordInput)
    name = forms.CharField(label='company Name')
    about = forms.CharField(label='about')
    location = forms.CharField(label='location')
    company_website = forms.URLField(label='company website', required=False)

    def clean_password2(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 and password2 and password1 != password2:
            raise ValueError("passwords don't match with one another.")
        return password2




