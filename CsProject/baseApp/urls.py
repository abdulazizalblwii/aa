from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('FQA/', views.FQA, name='FQA'),
    path('CoursesList/', views.CoursesList, name='CoursesList'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]
