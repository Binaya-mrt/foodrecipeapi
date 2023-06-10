from django.db import models
import uuid

# Pillow is used to add image

class Resturant(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=120,unique=True,verbose_name='Name')
    direction=models.CharField(max_length=120,verbose_name='Direction')
    phone=models.IntegerField()

    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    name=models.CharField(max_length=120,verbose_name='Recipe-Name')
    type=models.CharField(max_length=120,choices=[('BREAKFAST', 'Breakfast'), ('LUNCH', 'Lunch'), ('COFFEE', 'Coffee'),
                                     ('DINNER', 'Dinner')])
    thumbnail=models.ImageField(upload_to='recipe_thumbnail',default='recipe_thumbnail/default.png')
    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    recipe=models.ManyToManyField(Recipe)
    name=models.CharField(max_length=120,unique=True,verbose_name='Name')

    def __str__(self):
        return self.name
