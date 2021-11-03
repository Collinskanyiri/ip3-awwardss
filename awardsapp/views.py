from django.shortcuts import render
from .forms import SignupForm,UpdateUserForm, UpdateProfileForm, ReviewForm,ProjectForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile,Project,Review
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets,permissions
from .serializers import ProfileSerializer, ProjectSerializer,UpdateProjectSerializer, ReviewSerializer,ShowProjectSerializer,CreateProjectSerializer,DetailedProjectSerializer,ShowLikeSerializer,CreateLikeSerializer
# Create your views here.
def signup(request):
    name = 'Signup'
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form, 'name': name})

@login_required(login_url='/login/')
def profile(request):
    current_user = request.user

    return render(request, 'profile.html', {'current_user': current_user, })

@login_required(login_url='/login/')
def update_profile(request):
    current_user = request.user
    profile = Profile(user=request.user)
   
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES,  instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user= current_user
            profile.save()
        return redirect('home')
    else:
        form = UpdateProfileForm(instance=request.user.profile)
        args = {}
        # args.update(csrf(request))
        args['form'] = form
    return render(request, 'update_profile.html', {'current_user':current_user, 'form':form})

class ProfileViewset(viewsets.ModelViewSet):
    
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes=[permissions.AllowAny]

class ProjectViewset(viewsets.ModelViewSet):
    
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer,{
        'show': ShowProjectSerializer,
        'create': CreateProjectSerializer,
        'update': UpdateProjectSerializer,
        'detailed': DetailedProjectSerializer,
         }
    permission_classes=[permissions.AllowAny]
    def create(self, request, *args, **kwargs):
        author = request.author
        request.data['author'] = author.pk
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        author = request.author
        request.data['author'] = author.pk
        return super().update(request, *args, **kwargs)

    
class ReviewViewset(viewsets.ModelViewSet):
    
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[permissions.AllowAny]

@login_required(login_url='login')
def project(request, project):
    project = Project.objects.get(title=project)
    review = Review.objects.filter(user=request.user, project=project).first()
    rating_status = None
    if review is None:
        rating_status = False
    else:
        rating_status = True
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.post = project
            rate.save()
            post_ratings = Review.objects.filter(project=project)

            design_ratings = [d.design for d in post_ratings]
            design_average = sum(design_ratings) / len(design_ratings)

            usability_ratings = [us.usability for us in post_ratings]
            usability_average = sum(usability_ratings) / len(usability_ratings)

            content_ratings = [content.content for content in post_ratings]
            content_average = sum(content_ratings) / len(content_ratings)

            score = (design_average + usability_average + content_average) / 3
            print(score)
            rate.design_average = round(design_average, 2)
            rate.usability_average = round(usability_average, 2)
            rate.content_average = round(content_average, 2)
            rate.score = round(score, 2)
            rate.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = RatingsForm()
    params = {
        'post': post,
        'rating_form': form,
        'rating_status': rating_status

    }
    return render(request, 'project.html', params)