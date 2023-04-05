from django.urls import path
from .views import ProfileAPIView

urlpatterns = [
    path('login', ProfileAPIView.as_view({
    'post': 'login'
    })),
    path('admin', ProfileAPIView.as_view({
    'post': 'is_admin'
    }))
]