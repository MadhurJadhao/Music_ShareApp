from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('home', views.homepage, name='homepage'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('upload/', views.upload_file, name='upload_file'),
]
