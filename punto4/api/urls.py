from django.urls import path
from .views import ElementAPIView

urlpatterns = [
  path('elements/', ElementAPIView.as_view(), name='element-list-create'),
  path('elements/<int:id>/', ElementAPIView.as_view(), name='element-retrieve-update-delete'),
]

