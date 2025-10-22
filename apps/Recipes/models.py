from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50)
    recipe_des = models.TextField(max_length=1000)
    recipe_image = models.ImageField(upload_to="recipies/")

    def __str__(self):
        return self.recipe_name