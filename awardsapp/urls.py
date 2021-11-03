from django.urls import path, include
from . import views
from rest_framework import routers
from awardsapp import views



router = routers.DefaultRouter()
router.register('users', views.ProfileViewset)
router.register('project', views.ProjectViewset)
router.register('profile', views.ReviewViewset)




urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/update', views.update_profile, name='update_profile'),
    path('project/<review>', views.project_review, name='project_review'),
    path('search/', views.search_project, name='search'),
]
