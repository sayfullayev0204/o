from django.urls import path
from .views import VideoListCreateView, VideoRetrieveUpdateDestroyView

urlpatterns = [
    path('videos/', VideoListCreateView.as_view(), name='list_create'),
    path('videos/<int:pk>/', VideoRetrieveUpdateDestroyView.as_view(), name='update'),
]
