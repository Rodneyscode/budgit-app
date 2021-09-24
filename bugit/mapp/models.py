from django.db import models

class TestMod(models.Model):
	words = models.CharField(max_length=40)
	wordstwo = models.CharField(max_length=40)

	def __str__(self):
		return self.words






