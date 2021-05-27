from django.contrib import admin
from . import models

# from .models import Privacy


admin.site.register(models.Post)
admin.site.register(models.Recipes)

# admin.site.register(models.Privacy)

