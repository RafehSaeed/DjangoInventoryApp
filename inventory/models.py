from __future__ import unicode_literals

from django.db import models

class item(models.Model):

	title  = models.CharField(max_length=200)
	description =  models.TextField()
	amount = models.IntegerField()

