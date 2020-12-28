from django.urls import path
from .views import CreatePost, RetrieveUpdateDestroyPost

urlpatterns = [
    path('', CreatePost.as_view(), name='create'),
    path('<int:pk>/', RetrieveUpdateDestroyPost.as_view(), name='retrieve_update_destroy'),
]
