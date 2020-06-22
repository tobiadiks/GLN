from django.db import models

from django.utils import timezone
class Sermon(models.Model):


	title = models.CharField(max_length = 256, unique = True)
	
	author = models.CharField(max_length= 40)
	date = models.DateTimeField(default = timezone.now)
	summary = models.TextField(max_length = 1500, help_text = 'not more than 1500 words')
	video_link = models.URLField()
	photo = models.URLField(default = 'insert photo link here')
	slug = models.SlugField()
	
	def __str__(self):
		return self.title
	class Meta:
		ordering = ['-date']
# Create your models here.
