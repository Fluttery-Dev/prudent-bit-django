from .views import hello, GetAllPosts, getPost
from django.urls import path

urlpatterns = [
    path('', hello),
    path('allPosts', GetAllPosts),
    path('post/<slug:slug>', getPost)
]
