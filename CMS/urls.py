from django.urls import path
from .views import ResourceAPIView

urlpatterns = [
    path('gdd', ResourceAPIView.as_view({
    'get': 'list_gdd',
    })),
    path('gad', ResourceAPIView.as_view({
    'get': 'list_gad'
    })),
    path('gsd', ResourceAPIView.as_view({
    'get': 'list_gsd'
    })),
    path('resources', ResourceAPIView.as_view({
    'post': 'add_resource'
    }))
]
