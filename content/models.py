from django.db import models

# Create your models here.
class ImageContent(models.Model):
	ethnicity = models.CharField(max_length = 200)
	imagePath = models.ImageField()

	def __str__(self):
		return self.ethnicity