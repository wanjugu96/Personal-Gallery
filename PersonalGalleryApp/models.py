from django.db import models

# Create your models here.
class Location(models.Model):
    name=models.CharField(max_length=100)

class Category(models.Model):
    name=models.CharField(max_length=100)

class Image(models.Model):
    imagepath=models.ImageField(upload_to = 'galleryPhotos/')
    name=models.CharField(max_length=100)
    description=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    
