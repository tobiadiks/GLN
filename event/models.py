from django.db import models
from django.utils import timezone

class Event(models.Model):
	event = models.CharField(max_length = 200)
	image = models.URLField()
	venue = models.CharField(max_length = 50)
	address = models.TextField()
	start = models.DateTimeField(default = timezone.now)
	end = models.DateTimeField(default = timezone.now)
	
	def __str__(self):
		return self.event
		
		
	class Meta:
		ordering = ['start']
# Create your models here.
