from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    username=models.CharField(max_length=155)
    profile_photo=models.ImageField(upload_to='image')
    bio=models.CharField(max_length=255)
    projects=models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.username}Profile '

    def save_profile(self):
        self.save()

class Project(models.Model):
    project_name= models.CharField(max_length=100 )
    description=models.CharField(max_length=500)
    project_img=models.ImageField(upload_to='image')
    project_url=models.URLField(max_length=200)
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.project_name

    def save_project(self):
        self.save()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f'Like: {self.profile.user} | {self.project.project_name}'

class Review(models.Model):
    Rating=[
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (10,'10'),
    ]
    project_perfomance=models.IntegerField(choices=Rating, default='1' )
    Design=models.IntegerField(choices=Rating, default='1' )
    Usability=models.IntegerField(choices=Rating, default='1' )
    Content=models.IntegerField(choices=Rating, default='1' )

def mean(self):
            sum=0
            sum=(self.Design + self.Usability   + self.Content)
            avg= (sum/3)
            return avg
            
average=property(mean)
