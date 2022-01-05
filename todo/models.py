from django.db import models

# Create your models here.

class Todo(models.Model):
	title=models.CharField(max_length=1000)
	date=models.DateTimeField('date published')

	def __str__(self):
		return f"{self.title} created on {self.date}"
		
