from django.db import models

'''py.exe .\manage.py makemigrations --- makemigrations tells check the models.py and create those models'''


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)  # blank tells it could be blank

