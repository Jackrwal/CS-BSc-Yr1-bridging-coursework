from django.urls import path
from . import views

# set root to be the post list view
urlpatterns = [
    path('', views.postList, name='post-list'),
]