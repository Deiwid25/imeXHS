from django.urls import path
from .views import ElementListCreateAPIView, ElementDetailAPIView

urlpatterns = [
  path('elements/', ElementListCreateAPIView.as_view(), name='element-list-create'),
  path('elements/<str:id>/', ElementDetailAPIView.as_view(), name='element-retrieve-update-delete'),
]
