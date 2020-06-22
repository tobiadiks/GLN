from django.db import models

class Database(models.Model):
	Name = models.CharField(max_length = 60)
	address = models.TextField()
	phone = models.CharField(max_length = 13)
	
	def __str__(self):
		return self.Name
	

# Create your models here.
