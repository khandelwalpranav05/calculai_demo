from django.db import models

# Create your models here.
class ImageContent(models.Model):
	enthnicity = models.CharField(max_length = 10)
	imagePath = models.ImageField()

	def __str__(self):
		return self.enthnicity