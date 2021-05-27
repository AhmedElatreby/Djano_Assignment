from django.shortcuts import render

from .models import Post, Recipes

def home(request):
    data = Post.objects.all()
    return render(request, "index.html", {"posts": data})

def single(request, slug):
    data = Post.objects.get(slug=slug)
    return render(request, "single.html", {"post": data})

def aboutus(request):
    return render(request, "aboutus.html", {})

def recipes_list(request):
    recipes = Recipes.objects.all()
    return render(request, "recipes.html", {"recipes": recipes})      

    