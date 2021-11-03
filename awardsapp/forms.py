from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project,Profile, Review

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('email' ,'username','password1', 'password2', )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'projects', 'profile_photo', 'bio', 'contact']  

    class Meta:
        model = Project
        fields = ('project_img', 'project_name', 'project_url', 'description')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['Design', 'Usability', 'Content']   

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_img', 'project_name', 'project_url', 'description')