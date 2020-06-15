from django.urls import path
from . import views

# url root set to post list
# create end-points for each post
urlpatterns = [
    path('', views.postList, name='post-list'),
    path('post/<int:pk>/', views.post, name='post'),
    path('post/new', views.newPost, name='postNew'),
    path('post/<int:pk>/edit', views.editPost, name='postEdit')
]