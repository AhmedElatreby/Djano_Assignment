from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name="Fresher"

urlpatterns = [
    path('', views.home, name="homepage"),
    path('single/<slug:slug>', views.single, name="single"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('recipes /', views.recipe_list, name="recipe_list"),
]