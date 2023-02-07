from django.urls import path
from . import views

urlpatterns = [
    path('', views.cms),
    path('GDD/', views.gdd_view, name="GDD"),
    path('GSD/', views.gsd_view, name="GSD"),
    path('GAD/', views.gad_view, name="GAD")
]
