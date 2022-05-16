from django.urls import path
from . import views 


urlpatterns = [
    path('partenaires', views.partenaires, name="partenaires"),
    path('videos', views.videos, name="videos"),
]