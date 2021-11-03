from rest_framework import serializers
from .models import Profile, Project, Review




class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model =Review
        fields=[
            'project_perfomance',
            'Design',
            'Usability',
            'Content',
        
        ]

class ProjectSerializer(serializers.ModelSerializer):
    proj_performance=ReviewSerializer(read_only=True, many=True)
    class Meta:
        model=Project
        fields=[
            'user',
            'project_name',
            'description',
            'project_img',
            'project_url',
            'proj_performance'
        ]


class ProfileSerializer(serializers.ModelSerializer):
    projects=ProjectSerializer(read_only=True, many=True)
    class Meta:
        model=Profile
        fields=[
            'user',
            'username',
            'profile_photo',
            'bio',
            'projects',
        ]


class ShowProjectSerializer(serializers.ModelSerializer):
    
    Profile = ProfileSerializer

    class Meta:
        model = Project
        exclude = ('content',)
        depth = 1


class CreateProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = '__all__'
        extra_kwargs = {'image': {'required': False, 'allow_null': True}}

class UpdateProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = '__all__'
               


class DetailedProjectSerializer(serializers.ModelSerializer):
    
    Profile = ProfileSerializer
    class Meta:
        model = Project
        fields = '__all__'
        depth = 1


