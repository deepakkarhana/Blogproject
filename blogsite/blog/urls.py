from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('create/', views.create_post, name='create_post'),
]