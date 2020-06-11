from django.urls import path
from . import views

# url root set to post list
# create end-points for each post
urlpatterns = [
    path('', views.postList, name='post-list'),
    path('post/<int:pk>/', views.post, name='post'),
]