from django.urls import path

from . import views

app_name = "fresher"

urlpatterns = [
    path('', views.home, name="homepage"),
    path('single/<slug:slug>', views.single, name="single"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('recipe/<title:title>', views.recipe_list, name="recipes"),
]
