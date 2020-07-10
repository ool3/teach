from django.db import models

# Create your models here.
class List(models.Model):
	title = models.CharField(max_length=200)

	def __str__(self):
		return self.title

class Book(models.Model):
	list_book = models.ForeignKey(List, on_delete=models.CASCADE)
	title = models.CharField(max_length=150)
	author = models.CharField(max_length=200)
	url = models.URLField(max_length=200,null=True, blank=True)

	def __str__(self):
		return '{} | {}'.format(self.title, self.author)
