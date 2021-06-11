from django.urls import path
from django.urls.resolvers import URLPattern
from .views import TaskAPIView

urlpatterns = [
    path('api/', TaskAPIView.as_view())
]