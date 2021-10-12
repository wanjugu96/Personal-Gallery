from django.db import models

# Create your models here.
class Location(models.Model):
    name=models.CharField(max_length=100)

class Category(models.Model):
    name=models.CharField(max_length=100)

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


    def get_image_by_id(self,id):
        Image.objects.get(id=id)

    def search_image(self,category):
        Image.objects.filter(category=category)    



    def filter_by_location(self,location):
        Image.objects.filter(location=location)    
    
