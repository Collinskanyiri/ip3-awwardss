from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    username=models.CharField(max_length=155)
    profile_photo=models.ImageField(upload_to='image')
    bio=models.CharField(max_length=255)
    projects=models.CharField(max_length=255)
    contact = models.EmailField(max_length=100, blank=True)
    
    def __str__(self):
        return f'{self.user.username}Profile '

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self,):
        self.save()

    @classmethod
    def get_profile_by_user(cls, user):
        profile = cls.objects.filter(user=user)
        return profile    

class Project(models.Model):
    project_name= models.CharField(max_length=100 )
    description=models.CharField(max_length=500)
    project_img=models.ImageField(upload_to='image')
    project_url=models.URLField(max_length=200)
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.project_name

    def save_project(self):
        self.save()

    def delete_project(self):
            self.delete()    
    @classmethod
    def search_project(cls, title):
        return cls.objects.filter(title__icontains=title).all()

    @classmethod
    def all_projects(cls):
        return cls.objects.all()

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
    score = models.FloatField(default=0, blank=True)
    
    def __str__(self):
        return f'{self.project} Review'

    def mean(self):
            sum=0
            sum=(self.Design + self.Usability   + self.Content)
            score= (sum/3)
            return score
    score=property(mean)

    def save_rating(self):
        self.save()