from django.contrib import admin

from .models import Recipe,Resturant,Ingredient

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Resturant)
admin.site.register(Ingredient)