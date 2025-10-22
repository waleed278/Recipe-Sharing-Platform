from django.contrib import admin
from .models import Recipe
# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe_name','recipe_des','recipe_image')

admin.site.register(Recipe,RecipeAdmin)