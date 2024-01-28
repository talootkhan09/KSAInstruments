from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='region_images/', null=True, blank=True)
    instrument= models.CharField(max_length=100)
    youtube_link=models.CharField(max_length=100)