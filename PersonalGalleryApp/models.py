from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Location(models.Model):
    name=models.CharField(max_length=100)
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

class Category(models.Model):
    name=models.CharField(max_length=100)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

class Image(models.Model):
    imagepath=models.ImageField(upload_to = 'galleryPhotos/')
    name=models.CharField(max_length=50)
    description=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self,id,imagepath):
       Image.objects.filter(id = id).update(imagepath =imagepath)

    @classmethod
    def get_image_by_id(cls,id):
        animage=cls.objects.filter(id=id)
        return animage
    
    @classmethod
    def search_image(cls,search_term):
        

        images=cls.objects.filter(category__name__icontains=search_term)  
        return images 


    @classmethod
    def filter_by_location(cls,location):
        images=cls.objects.filter(location=location)    

        return images
    @classmethod
    def allimages(cls):
        images=cls.objects.all()    

        return images
        
    
