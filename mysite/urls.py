"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import index
from myapp.views import mentor_registration, mentee_registration
from apps.clubs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('register/mentor/', mentor_registration, name='mentor_registration'),
    path('register/mentee/', mentee_registration, name='mentee_registration'),
    path('clubs', views.clubs_list_view, name='clubs-list'),
    path('editClub/<int:club_id>/', views.edit_club, name='edit_club'),
    path('createClub', views.create_club_view, name='create_club'),
]
