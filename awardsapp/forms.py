from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project, Projects, Profile, Review, Reviews
from pyuploadcare.dj.forms import ImageField


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('user', 'email', 'password1', 'password2')

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('user', 'email')

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'projects', 'profile_photo', 'bio', 'contact']  

class ProjectForm(forms.ModelForm):
    project_img = ImageField(label='')

    class Meta:
        model = Project
        fields = ('project_img', 'project_name', 'project_url', 'description')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['Design', 'Usability', 'Content']        