from django.urls import path
from . import views

urlpatterns = [
    path('courselistpage/', views.courselistpage, name='courselistpage'),
    path('course_search/', views.course_search, name='coursesearch'),
]