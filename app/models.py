from django.db import models

# Create your models here.

class Home(models.Model):
    image=models.ImageField(upload_to="home_paage_images")
    left=models.ImageField(upload_to="home_paage_images")
    right=models.ImageField(upload_to="home_paage_images")

class Contact(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
    subject=models.CharField(max_length=100)
    message=models.TextField()
    def __str__(self):
        return self.name

class Gallery(models.Model):
    image=models.ImageField(upload_to="gallery_images")
