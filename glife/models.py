from django.db import models
from django.utils import timezone

class Home_Verse(models.Model):
	bible_quote = models.TextField( help_text = 'e.g John 3:16, include quote')
	
	
	def __str__(self):
		return self.bible_quote
	
	
	
class Service(models.Model):
	service = models.TextField()
	start = models.TimeField(default = timezone.now)
	end = models.TimeField(default = timezone.now)
	def __str__(self):
		return self.service
		
class Leader(models.Model):
	name = models.CharField(max_length = 30)
	photo = models.URLField(help_text = 'path to image url')
	phone = models.CharField(max_length =13)
	email = models.EmailField(max_length = 256)
	manifesto = models.CharField(max_length = 300)
	def __str__(self):
		return self.name

class Gallery(models.Model):
	name=models.CharField(max_length=10)
	image = models.URLField()
# Create your models here.


