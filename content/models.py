from django.db import models

# Create your models here.
class ImageContent(models.Model):
	enthnicity = models.CharField(max_length = 10)
	imagePath = models.ImageField(upload_to = 'media/content')