from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
	"""docstring for Post"""
	author=models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title=models.CharField(max_length=200)
	created_date=models.DateTimeField(default=timezone.now)
	published_date=models.DateTimeField(blank=True, null=True)
	text=models.TextField()

def publish(self):
	self.published_date=timezone.now()
	self.save()

def str(self):
	return self.title



# Create your models here.
