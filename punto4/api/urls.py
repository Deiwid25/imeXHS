from django.urls import path
from .views import ElementAPIView

urlpatterns = [
  path('elements/', ElementAPIView.as_view(), name='element-list-create'),
  path('elements/<str:id>/', ElementAPIView.as_view(), name='element-retrieve-update-delete'),
]

